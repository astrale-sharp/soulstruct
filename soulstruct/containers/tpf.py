from __future__ import annotations

__all__ = ["TPFTexture", "TPF"]

import logging
import json
import re
import shutil
import tempfile
import typing as tp
import zlib
from enum import IntEnum
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.base.textures.dds import DDS, DDSCAPS2, texconv, convert_dds_file
from soulstruct.utilities.binary import BinaryReader, BinaryWriter
from .dcx import decompress

_LOGGER = logging.getLogger(__name__)


class TPFPlatform(IntEnum):
    PC = 0
    Xbox360 = 1
    PS3 = 2
    PS4 = 4
    XboxOne = 5


class TextureType(IntEnum):
    Texture = 0  # one 2D texture
    Cubemap = 1  # six 2D textures
    Volume = 2  # one 3D texture


class TextureHeader:
    """Extra metadata for headerless textures used in console versions."""
    width: int
    height: int
    texture_count: int
    unk1: int  # unknown, PS3 only
    unk2: int  # unknown, 0x0 or 0xAAE4 in DeS, 0xD in DS3 (console)
    dxgi_format: int  # Microsoft DXGI_FORMAT


class FloatStruct:
    """Unknown optional data for some textures."""
    unk0: int
    values: list[float]

    @classmethod
    def unpack_from(cls, reader: BinaryReader):
        float_struct = cls()
        float_struct.unk0 = reader.unpack_value("i")
        length = reader.unpack_value("i")
        if length < 0 or length % 4:
            raise ValueError(f"Unexpected `FloatStruct` length: {length}. Expected a multiple of 4 (or 0).")
        float_struct.values = list(reader.unpack(f"{length // 4}f"))

    def pack(self, writer: BinaryWriter):
        writer.pack("i", self.unk0)
        writer.pack("i", len(self.values) * 4)
        writer.pack(f"{len(self.values)}f", *self.values)


class TPFTexture:

    name: str
    format: int
    texture_type: TextureType
    mipmaps: int
    texture_flags: int  # {2, 3} -> DCX-compressed; unknown otherwise
    data: bytes
    header: tp.Optional[TextureHeader]
    float_struct: tp.Optional[FloatStruct]

    def __init__(self):
        self.name = ""
        self.format = 1
        self.texture_type = TextureType.Texture
        self.mipmaps = 0
        self.texture_flags = 0
        self.data = b""
        self.header = None
        self.float_struct = None

    @classmethod
    def unpack_from(
        cls,
        reader: BinaryReader,
        platform: TPFPlatform,
        tpf_flags: int,
        encoding: str,
    ):
        self = cls()

        file_offset = reader.unpack_value("I")
        file_size = reader.unpack_value("i")

        self.format = reader.unpack_value("B")
        self.texture_type = TextureType(reader.unpack_value("B"))
        self.mipmaps = reader.unpack_value("B")
        self.texture_flags = reader.unpack_value("B")
        if self.texture_flags not in {0, 1, 2, 3}:
            raise ValueError(f"`TPFTexture.flags1` was {self.texture_flags}, but expected 0, 1, 2, or 3.")

        if platform != TPFPlatform.PC:
            self.header = TextureHeader
            self.header.width = reader.unpack_value("h")
            self.header.height = reader.unpack_value("h")
            if platform == TPFPlatform.Xbox360:
                reader.assert_pad(4)
            elif platform == TPFPlatform.PS3:
                self.header.unk1 = reader.unpack_value("i")
                if tpf_flags != 0:
                    self.header.unk2 = reader.unpack_value("i")
                    if self.header.unk2 not in {0, 0x68E0, 0xAAE4}:
                        raise ValueError(
                            f"`TextureHeader.unk2` was {self.header.unk2}, but expected 0, 0x68E0, or 0xAAE4."
                        )
            elif platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
                self.header.texture_count = reader.unpack_value("i")
                if self.header.texture_count not in {1, 6}:
                    f"`TextureHeader.texture_count` was {self.header.texture_count}, but expected 1 or 6."
                self.header.unk2 = reader.unpack_value("i")
                if self.header.unk2 != 0xD:
                    f"`TextureHeader.unk2` was {self.header.unk2}, but expected 0xD."

        name_offset = reader.unpack_value("I")
        has_float_struct = reader.unpack_value("i") == 1
        if platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
            self.header.dxgi_format = reader.unpack_value("i")
        if has_float_struct:
            self.float_struct = FloatStruct.unpack_from(reader)

        with reader.temp_offset(file_offset):
            self.data = reader.read(file_size)
        if self.texture_flags in {2, 3}:
            # Data is DCX-compressed.
            # TODO: should enforce DCX type as 'DCP_EDGE'?
            self.data = decompress(self.data)

        self.name = reader.unpack_string(offset=name_offset, encoding=encoding)

        return self

    def pack_header(self, writer: BinaryWriter, index: int, platform: TPFPlatform, tpf_flags: int):
        if platform == TPFPlatform.PC:
            dds = self.get_dds()
            if dds.header.caps_2 & DDSCAPS2.CUBEMAP:
                tex_type = TextureType.Cubemap
            elif dds.header.caps_2 & DDSCAPS2.VOLUME:
                tex_type = TextureType.Volume
            else:
                tex_type = TextureType.Texture
            mipmap_count = dds.header.mipmap_count
        else:
            tex_type = self.texture_type
            mipmap_count = self.mipmaps

        writer.reserve(f"file_data_{index}", "I")
        writer.reserve(f"file_size_{index}", "i")
        writer.pack("b", self.format)
        writer.pack("b", tex_type)
        writer.pack("b", mipmap_count)
        writer.pack("b", self.texture_flags)

        if platform != TPFPlatform.PC:
            writer.pack("h", self.header.width)
            writer.pack("h", self.header.height)
            if platform == TPFPlatform.Xbox360:
                writer.pad(4)
            elif platform == TPFPlatform.PS3:
                writer.pack("i", self.header.unk1)
                if tpf_flags != 0:
                    writer.pack("i", self.header.unk2)
            elif platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
                writer.pack("i", self.header.texture_count)
                writer.pack("i", self.header.unk2)

        writer.reserve(f"file_name_{index}", "I")
        writer.pack("i", 0 if self.float_struct is None else 1)

        if platform in {TPFPlatform.PS4, TPFPlatform.XboxOne}:
            writer.pack("i", self.header.dxgi_format)

        if self.float_struct:
            self.float_struct.pack(writer)

    def pack_name(self, writer: BinaryWriter, index: int, encoding: int):
        writer.fill(f"file_name_{index}", writer.position)
        if encoding == 1:
            name = self.name.encode(encoding="utf-16-be" if writer.big_endian else "utf-16-le") + b"\0\0"
        elif encoding in {0, 2}:
            name = self.name.encode(encoding="shift-jis") + b"\0"
        else:
            raise ValueError(f"Invalid TPF texture encoding: {encoding}. Must be 0, 1, or 2.")
        writer.append(name)

    def pack_data(self, writer: BinaryWriter, index: int):
        writer.fill(f"file_data_{index}", writer.position)
        if self.texture_flags in {2, 3}:
            data = zlib.compress(self.data, level=7)
        else:
            data = self.data

        writer.fill(f"file_size_{index}", len(data))
        writer.append(data)

    def get_dds(self) -> DDS:
        return DDS(self.data)

    def get_dds_format(self) -> str:
        return DDS(self.data).header.fourcc.decode()

    def write_dds(self, dds_path: str | Path):
        Path(dds_path).write_bytes(self.data)

    def get_png_data(self, fmt="rgba") -> bytes:
        with tempfile.TemporaryDirectory() as png_dir:
            temp_dds_path = Path(png_dir, "temp.dds")
            temp_dds_path.write_bytes(self.data)
            texconv_result = texconv("-o", png_dir, "-ft", "png", "-f", fmt, temp_dds_path)
            try:
                return Path(png_dir, "temp.png").read_bytes()
            except FileNotFoundError:
                stdout = "\n    ".join(texconv_result.stdout.decode().split("\r\n")[3:])  # drop copyright lines
                raise ValueError(f"Could not convert texture DDS to PNG:\n    {stdout}")

    def export_png(self, png_path: str | Path, fmt="rgba"):
        png_data = self.get_png_data(fmt)
        png_path.write_bytes(png_data)

    def convert_dds_format(self, output_format: str, assert_input_format: str = None) -> bool:
        """Convert `data` DDS format in place. Returns `True` if conversion succeeds."""
        dds = self.get_dds()
        current_format = dds.header.fourcc.decode()
        current_dxgi_format = dds.dxt10_header.dxgi_format if dds.dxt10_header else None
        if assert_input_format is not None and current_format != assert_input_format.encode():
            raise ValueError(
                f"TPF texture DDS format {current_format} does not match "
                f"`assert_input_format` {assert_input_format} ({current_format}"
            )
        temp_dds_path = Path(__file__).parent / "__temp__.dds"
        temp_dds_path.write_bytes(self.data)
        result = convert_dds_file(temp_dds_path, Path(__file__).parent, output_format)  # overwrite temp file
        if result.returncode == 0:
            self.data = temp_dds_path.read_bytes()
            if current_dxgi_format:
                _LOGGER.info(
                    f"Converted TPF texture {self.name} from format {current_format} "
                    f"(DXGI {current_dxgi_format}) to {output_format}."
                )
            else:
                _LOGGER.info(f"Converted TPF texture {self.name} from format {current_format} to {output_format}.")
            return True
        else:
            _LOGGER.error(
                f"Could not convert TPF texture {self.name} from format {current_format} to {output_format}.\n"
                f"   stdout: {result.stdout}\n"
                f"   stderr: {result.stderr}"
            )
            return False

    def __repr__(self) -> str:
        return (
            f"TPFTexture(\n"
            f"    name = '{self.name}'\n"
            f"    format = {self.format}\n"
            f"    texture_type = {self.texture_type.name}\n"
            f"    mipmaps = {self.mipmaps}\n"
            f"    texture_flags = {self.texture_flags}\n"
            f"    data = <{len(self.data)} bytes>\n"
            f"    has_header = {self.header is not None}\n"
            f"    has_float_struct = {self.float_struct is not None}\n"
            f")"
        )


class TPF(GameFile):

    textures: list[TPFTexture]
    platform: TPFPlatform
    encoding: int
    tpf_flags: int  # non-zero value on PS3 means textures have `unk2`; unknown otherwise

    def unpack(self, reader: BinaryReader, **kwargs):
        reader.unpack_value("4s", asserted=b"TPF\0")
        self.platform = TPFPlatform(reader.unpack_value("B", offset=0xC))
        reader.byte_order = ">" if self.platform in {TPFPlatform.Xbox360, TPFPlatform.PS3} else "<"

        reader.unpack_value("i")  # data length
        file_count = reader.unpack_value("i")
        reader.unpack_value("B")  # platform
        self.tpf_flags = reader.unpack_value("B")
        if self.tpf_flags not in {0, 1, 2, 3}:
            raise ValueError(f"`TPF.tpf_flags` was {self.tpf_flags}, but expected 0, 1, 2, or 3.")
        self.encoding = reader.unpack_value("B")
        if self.encoding not in {0, 1, 2}:
            raise ValueError(f"`TPF.encoding` was {self.encoding}, but expected 0, 1, or 2.")
        reader.assert_pad(1)

        encoding = reader.get_utf_16_encoding() if self.encoding == 1 else "shift_jis_2004"
        self.textures = [
            TPFTexture.unpack_from(reader, self.platform, self.tpf_flags, encoding) for _ in range(file_count)
        ]

    def pack(self) -> bytes:
        """Pack TPF file to bytes."""
        writer = BinaryWriter(big_endian=self.platform in {TPFPlatform.Xbox360, TPFPlatform.PS3})
        writer.append(b"TPF\0")
        writer.reserve("data_size", "i")
        writer.pack("i", len(self.textures))
        writer.pack("b", self.platform)
        writer.pack("b", self.tpf_flags)
        writer.pack("b", self.encoding)
        writer.pad(1)

        for i, texture in enumerate(self.textures):
            texture.pack_header(writer, i, self.platform, self.tpf_flags)
        for i, texture in enumerate(self.textures):
            texture.pack_name(writer, i, self.encoding)

        data_start = writer.position
        for i, texture in enumerate(self.textures):
            # TKGP notes: padding varies wildly across games, so don't worry about it too much.
            if len(texture.data) > 0:
                writer.pad_align(4)
            texture.pack_data(writer, i)
        writer.fill("data_size", writer.position - data_start)
        return writer.finish()

    def write_unpacked_dir(self, directory=None):
        if directory is None:
            if self.path:
                directory = self.path.with_suffix(self.path.suffix + ".unpacked")
            else:
                raise ValueError("Cannot detect `directory` for unpacked binder automatically.")
        else:
            directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)

        texture_entries = []
        for i, texture in enumerate(self.textures):
            texture_dict = {
                "name": texture.name,
                "format": texture.format,
                "texture_type": texture.texture_type.name,
                "mipmaps": texture.mipmaps,
                "texture_flags": texture.texture_flags,
            }
            texture_entries.append(texture_dict)
            texture.write_dds(directory / f"{Path(texture.name).stem}.dds")
        json_dict = self.get_json_header()
        json_dict["entries"] = texture_entries

        # NOTE: Binder manifest is always encoded in shift-JIS, not `shift_jis_2004`.
        with (directory / "tpf_manifest.json").open("w", encoding="shift-jis") as f:
            json.dump(json_dict, f, indent=4)

    def get_json_header(self):
        return {
            "platform": self.platform.name,
            "encoding": self.encoding,
            "tpf_flags": self.tpf_flags,
        }

    def convert_dds_formats(self, input_format: str, output_format: str):
        """Convert all DDS files that currently have format `input_format` to `output_format`.

        Formats should look like b"DX10", b"DXT1", etc.
        """
        fail_count = 0
        total_count = 0
        for texture in self.textures:
            dds = texture.get_dds()
            if dds.header.fourcc.decode() == input_format:
                success = texture.convert_dds_format(output_format)
                total_count += 1
                if not success:
                    fail_count += 1
        if fail_count > 0:
            _LOGGER.warning(
                f"Failed to convert {fail_count} out of {total_count} textures from {input_format} to {output_format}."
            )

    def get_all_png_data(self, fmt="rgba") -> list[tp.Optional[bytes]]:
        png_datas = []
        for tex in self.textures:
            try:
                png_datas.append(tex.get_png_data(fmt))
            except ValueError as ex:
                _LOGGER.warning(str(ex))
                png_datas.append(None)
        return png_datas

    def export_to_pngs(self, png_dir_path: Path | str, fmt="rgba"):
        for tex in self.textures:
            png_name = Path(tex.name).with_suffix(".png")
            try:
                tex.export_png(png_dir_path / png_name, fmt=fmt)
            except ValueError as ex:
                _LOGGER.warning(str(ex))

    def __repr__(self) -> str:
        return (
            f"TPF(\n"
            f"    textures = <{len(self.textures)} textures>\n"
            f"    platform = {self.platform.name}\n"
            f"    encoding = {self.encoding}\n"
            f"    tpf_flags = {self.tpf_flags}\n"
            f")"
        )

    @classmethod
    def collect_tpf_textures(
        cls, tpfbhd_directory: str | Path, convert_formats: tp.Tuple[str, str] = None
    ) -> dict[str, TPFTexture]:
        """Build a dictionary mapping TGA texture names to `TPFTexture` instances."""
        from soulstruct.containers import Binder

        tpf_re = re.compile(rf"(.*)\.tpf(\.dcx)?")
        tpfbhd_directory = Path(tpfbhd_directory)
        textures = {}
        for bhd_path in tpfbhd_directory.glob("*.tpfbhd"):
            bxf = Binder(bhd_path, create_bak_if_missing=False)
            for entry in bxf.entries:
                match = tpf_re.match(entry.name)
                if match:
                    tpf = cls(entry.data)
                    if convert_formats is not None:
                        input_format, output_format = convert_formats
                        tpf.convert_dds_formats(input_format, output_format)
                    for texture in tpf.textures:
                        textures[texture.name] = texture
        return textures
