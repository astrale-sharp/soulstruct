from __future__ import annotations

__all__ = ["FMG"]

import logging
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum
from textwrap import wrap

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *

try:
    Self = tp.Self
except AttributeError:
    Self = "FMG"

_LOGGER = logging.getLogger(__name__)


class FMGVersion(IntEnum):
    V0 = 0  # Demon's Souls
    V1 = 1  # Dark Souls, Dark Souls 2
    V2 = 2  # Bloodborne, Dark Souls 3, Sekiro, Elden Ring


GAME_MAX_LINES = {
    "darksouls1ptde": 11,
    "darksouls1r": 11,
}


@dataclass(slots=True)
class FMGHeader(NewBinaryStruct):
    _pad1: bytes = field(**BinaryPad(1))
    big_endian: bool
    version: FMGVersion = field(**Binary(byte))
    _pad2: bytes = field(**BinaryPad(1))
    file_size: int
    _one: byte = field(**Binary(asserted=1))
    unknown1: byte  # -1 for version 0, 0 for version 1/2
    _pad3: bytes = field(**BinaryPad(2))
    range_count: int
    string_count: int
    unknown2: int = field(**Binary(asserted=255, skip_callback=lambda _, values: values["version"] < 2))
    string_offsets_offset: varint
    _pad4: bytes = field(**BinaryPad(4))
    _pad5: bytes = field(**BinaryPad(4, skip_callback=lambda _, values: values["version"] < 2))


@dataclass(slots=True)
class FMG(GameFile):
    """Simple text dictionary.

    Since Demon's Souls, only the `version` field differs between games, with slight header structure changes.
    """

    EXT: tp.ClassVar[str] = ".fmg"

    entries: dict[int, str] = field(default_factory=dict)
    version: int = 2  # default to newest version (Bloodborne onwards)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:

        version = FMGVersion(reader.unpack_value("b", offset=2))
        reader.default_byte_order = ByteOrder.BigEndian if version == 0 else ByteOrder.LittleEndian
        reader.varint_size = 8 if version >= 2 else 4
        header = FMGHeader.from_bytes(reader)

        # Groups of contiguous text string IDs are defined by ranges (first ID, last ID) to save space.
        ranges = []
        for _ in range(header.range_count):
            first_index, first_id, last_id = reader.unpack("3i")
            if version == 2:
                reader.assert_pad(4)
            ranges.append((first_index, first_id, last_id))

        if reader.position != header.string_offsets_offset:
            _LOGGER.warning("Range data did not end at string data offset given in unpacked FMG header.")

        string_offsets = reader.unpack(f"{header.string_count}v")

        # Text pointer table corresponds to all the IDs (joined together) of the above ranges, in order.
        entries = {}
        for first_index, first_id, last_id in ranges:
            for string_id in range(first_id, last_id + 1):
                if string_id in entries:
                    raise ValueError(f"Malformed FMG: Text entry ID {string_id} appeared more than once.")
                string_offset = string_offsets[first_index]
                if string_offset == 0:
                    entries[string_id] = ""  # empty string (will trigger in-game error placeholder text)
                else:
                    entries[string_id] = reader.unpack_string(offset=string_offset, encoding="utf-16-le")
                first_index += 1

        return cls(entries, version)

    def sort(self):
        """Sort strings by ID in-place."""
        self.entries = {string_id: self.entries[string_id] for string_id in sorted(self.entries.keys())}

    def remove_empty_strings(self) -> FMG:
        """Remove all empty strings from entry dictionary and returns a copy.

        This will remove many entries from vanilla files, which (in older games at least) prefer defining entire ranges
        of strings even if only a few of them are used (which leads to smaller file sizes but makes dictionary versions
        of the data awkward).

        Returns a copy, e.g. if you only want to do it before packing.
        """
        new_entries = {string_id: string for string_id, string in self.entries.items() if string}
        return FMG(new_entries, self.version)

    def apply_line_limits(self, max_chars_per_line: int = None, max_lines: int = None) -> FMG:
        """Reformat strings to apply a word wrap limit and log a warning if line count exceeds `max_lines`. Returns a
        modified copy of the FMG.

        `max_lines` will be auto-detected by game by default. Set it to something stupidly high to disable it.
        """
        if max_lines is None:
            game = self.get_game()
            max_lines = GAME_MAX_LINES.get(game.submodule_name, None)

        new_entries = {}
        for string_id, string in self.entries.items():
            lines = string.split("\n\n")
            if lines in ["", " "]:
                new_entries[string_id] = string
                continue  # empty string or one-space string
            # Wrap lines, and re-add manual newlines.
            wrapped_lines = []
            for line in lines:
                if max_chars_per_line is None or "\n" in line:
                    # Don't touch lines with newlines already in them.
                    wrapped_lines.append(line)
                else:
                    wrapped_lines.append("\n".join(wrap(line, max_chars_per_line)))
            wrapped_string = "\n\n".join(wrapped_lines).rstrip("\n")
            line_count = wrapped_string.count("\n") + 1
            if max_lines is not None and line_count > max_lines - 1:
                _LOGGER.warning(
                    f"FMG string ID {string_id} has {line_count} lines (max is {max_lines}):\n"
                    f"{wrapped_string}"
                )
            new_entries[string_id] = wrapped_string
        return FMG(new_entries, self.version)

    def to_writer(self, sort=True) -> BinaryWriter:
        """Pack text dictionary to binary FMG file."""
        if sort:
            self.sort()

        writer = BinaryWriter(
            byte_order=ByteOrder.BigEndian if self.version == 0 else ByteOrder.LittleEndian,
            varint_size=8 if self.version >= 2 else 4,
        )

        FMGHeader.object_to_writer(
            self,
            writer,
            big_endian=self.version == 0,
            file_size=RESERVED,
            unknown1=-1 if self.version == 0 else 1,
            range_count=RESERVED,
            string_count=len(self.entries),
            string_offsets_offset=RESERVED,
        )

        # Construct ranges. A single missing ID will interrupt a range. (If empty strings from vanilla files have not
        # been removed, and no other IDs added/removed, these ranges should be identical to the vanilla ones.)

        range_count = 0
        range_start_index = first_id = last_id = None
        for string_index, string_id in enumerate(self.entries.keys()):
            if range_start_index is None:
                # Start new range at this string.
                range_start_index = string_index
                first_id = last_id = string_id
            elif string_id == last_id + 1:
                # Expand current range to include this string.
                last_id += 1
            else:
                # Terminate last range...
                writer.pack("3i", range_start_index, first_id, last_id)
                if self.version == 2:
                    writer.pad(4)
                range_count += 1
                # ... then start new one at this string.
                range_start_index = string_index
                first_id = last_id = string_id

        if first_id is not None:
            # Terminate final range.
            writer.pack("3i", range_start_index, first_id, last_id)
            if self.version == 2:
                writer.pad(4)
            range_count += 1
        writer.fill("range_count", range_count, self)

        writer.fill_with_position("string_offsets_offset", self)
        packed_strings = b""  # saving ourselves an additional iteration
        packed_strings_offset = writer.position + writer.varint_size * len(self.entries)
        for string_id, string in self.entries.items():
            if string == "":
                writer.pack("v", 0)  # no offset
            else:
                writer.pack("v", packed_strings_offset + len(packed_strings))
            packed_strings += string.encode("utf-16-le") + b"\0\0"

        writer.fill_with_position("file_size", self)

        return writer

    def __getitem__(self, index: int):
        return self.entries[index]

    def get(self, string_id: int, default: str = None):
        """Return `string_id` value or `default` if missing."""
        return self.entries.get(string_id, default)

    def __setitem__(self, index: int, text: str):
        self.entries[index] = text

    def setdefault(self, string_id: int, default: str):
        """Return `string_id` value or set it to `default` and return that."""
        return self.entries.setdefault(string_id, default)

    def pop(self, string_id: int, default: str = None):
        """Remove `string_id` value and return it, or return `default`.

        Will never raise a `KeyError`. Use `FMG.entries.pop()` if you want to assert the key exists.
        """
        return self.entries.pop(string_id, default)

    def update(self, fmg_or_entries: FMG | dict):
        """Update this FMG in place with `FMG` or `entries` dict."""
        if isinstance(fmg_or_entries, dict):
            return self.entries.update(fmg_or_entries)
        elif isinstance(fmg_or_entries, FMG):
            return self.entries.update(fmg_or_entries.entries)
        raise TypeError(f"Can only call `FMG.update()` with a dictionary or another `FMG`, not {type(fmg_or_entries)}.")

    def find(self, search_string: str, replace_with=None):
        """Search for the given text in this FMG.

        Args:
            search_string: Text to find. The text can appear anywhere inside an entry to return a result.
            replace_with: String to replace the given text with in any results. (Default: None)
        """
        found_something = False
        for index, text in self.entries.items():
            if search_string in text:
                if not found_something:
                    print(f"\n~~~ FMG: {str(self.path) if self.path is not None else '<None>'}")
                    found_something = True
                print(f"\n  [{index}]:\n{text}")
                if replace_with is not None:
                    self.entries[index] = text.replace(search_string, replace_with)
                    print(f"  -> {self.entries[index]}")
        if not found_something:
            print(f"Could not find any occurrences of string {repr(search_string)}.")

    def replace_substring_in_all(self, old_substring: str, new_substring: str) -> FMG:
        """Returns a copy off the FMG with all given substring replacements done.

        NOTE: Just a quieter, simpler version of calling `find` with `replace_with`.
        """
        new_entries = {
            string_id: string.replace(old_substring, new_substring)
            for string_id, string in self.entries
        }
        return FMG(new_entries, self.version)

    def __iter__(self):
        return iter(self.entries.items())

    def __repr__(self):
        s = f"FMG Path: {str(self.path) if self.path is not None else '<None>'}"
        for index, text in self.entries.items():
            s += f"\n    {index}: {text}"
        return s
