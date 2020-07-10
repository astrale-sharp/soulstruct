from __future__ import annotations

import logging
import math
import re
from ast import literal_eval
from enum import IntEnum
from typing import List, TYPE_CHECKING

from soulstruct.constants.darksouls1.maps import ALL_MAPS, get_map
from soulstruct.core import InvalidFieldValueError
from soulstruct.maps.core import MAP_ENTRY_TYPES
from soulstruct.maps.models import MSBModel
from soulstruct.models.darksouls1 import CHARACTER_MODELS
from soulstruct.project.utilities import bind_events, NameSelectionBox, EntryTextEditBox
from soulstruct.project.editor import SoulstructBaseFieldEditor
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.memory import MemoryHookError

if TYPE_CHECKING:
    from soulstruct.maps import DarkSoulsMaps
    from soulstruct.maps.base import MSBEntry

_LOGGER = logging.getLogger(__name__)

# TODO: Models are handled automatically. Model entries are auto-generated from all used model names.
#  - Validation is done by checking the model files for that map (only need to inspect the names inside the BND).
#  - Validation/SIB path depends on game version.
#  - Right-click pop-out selection list is available for characters (and eventually, some objects).


ENTRY_LIST_FG_COLORS = {
    'Parts': '#DDF',
    'Regions': '#FDD',
    'Events': '#DFD',
    'Models': '#FFC',
}


class SoulstructMapEditor(SoulstructBaseFieldEditor):
    DATA_NAME = "Maps"
    TAB_NAME = "maps"
    CATEGORY_BOX_WIDTH = 165
    ENTRY_BOX_WIDTH = 350
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 200
    FIELD_BOX_WIDTH = 500
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_COUNT = 37  # highest count (Parts.Collisions)
    FIELD_NAME_WIDTH = 20
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 60

    class FieldRow(SoulstructBaseFieldEditor.FieldRow):

        master: SoulstructMapEditor

        def __init__(self, editor: SoulstructMapEditor, row_index: int, main_bindings: dict = None):
            super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

            bg_color = self._get_color()

            self.value_vector_frame = editor.Frame(
                self.value_box, bg=bg_color, width=editor.FIELD_VALUE_WIDTH, height=editor.FIELD_ROW_HEIGHT,
                no_grid=True)
            bind_events(self.value_vector_frame, main_bindings)
            self.value_vector_x = editor.Label(
                self.value_vector_frame, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6,
                column=0, anchor='w')
            self.value_vector_y = editor.Label(
                self.value_vector_frame, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6,
                column=1, anchor='w')
            self.value_vector_z = editor.Label(
                self.value_vector_frame, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6,
                column=2, anchor='w')

            for coord, label in zip('xyz', (self.value_vector_x, self.value_vector_y, self.value_vector_z)):
                vector_bindings = main_bindings.copy()
                vector_bindings.update({
                    '<Button-1>': lambda _, c=coord: editor.select_displayed_field_row(row_index, coord=c)})
                bind_events(label, vector_bindings)

            self.unhide()

        def update_field(self, entry, name, nickname, value, field_type, docstring="DOC-TODO"):
            """Update widgets with given field information."""
            self.field_name = name
            self.field_type = field_type
            self.field_docstring = docstring

            # Nicknames are already formatted properly (i.e. not CamelCase).
            if self.field_name_label.var.get() != nickname:
                self.field_name_label.var.set(nickname)

            if isinstance(self.field_type, str):
                # Link could be an internal map entry name (will be converted to index on pack) or a param/text ID.
                # Note that the *argument* 'field_type' is used below, not attribute self.field_type.
                self.field_links = self.master.get_field_links(self.field_type, value)
                if not self.field_type.startswith('<Maps'):  # <Maps: or <MapsList:
                    field_type = int  # otherwise, leave as link string for first condition below
            else:
                self.field_links = []

            # Type checking order: [link_string, Vector, float/int/str, bool, list, IntEnum]
            if isinstance(field_type, str):
                if field_type.startswith('<MapsList:'):
                    value_text = "(select to edit)"
                    if self.field_links:
                        if len(self.field_links) > 1:
                            value_text += "  {AMBIGUOUS}"
                        if self.field_links[0].name is None:
                            value_text += "  {BROKEN LINK}"
                        else:
                            value_text += f"  {{{self.field_links[0].name}}}"
                    # TODO: better display? Pop-out?
                    self.value_label.var.set(value_text)
                else:
                    # Name of another MSB entry.
                    value_text = str(value)
                    if field_type == "<Maps:Models:Characters|Players>":
                        if self.field_links[0].name is None:
                            value_text += "  {BROKEN LINK}"
                        else:
                            model_id = int(value[1:])  # ignore 'c' prefix
                            try:
                                value_text += f"  {{{CHARACTER_MODELS[model_id]}}}"
                            except KeyError:
                                value_text += "  {UNKNOWN}"
                    self.value_label.var.set(value_text)
                self._activate_value_widget(self.value_label)

            elif field_type == Vector3:
                # No chance of a link here.
                self.value_vector_x.var.set(f'x: {value.x:.3f}')
                self.value_vector_y.var.set(f'y: {value.y:.3f}')
                self.value_vector_z.var.set(f'z: {value.z:.3f}')
                self._activate_value_widget(self.value_vector_frame)

            elif field_type in {float, int, str}:
                value_text = f'{value:.3f}' if field_type == float else str(value)
                if self.field_links:
                    if len(self.field_links) > 1:
                        value_text += "  {AMBIGUOUS}"
                    if self.field_links[0].name is None:
                        value_text += "  {BROKEN LINK}"
                    else:
                        value_text += f"  {{{self.field_links[0].name}}}"
                if self.value_label.var.get() != value_text:
                    self.value_label.var.set(value_text)
                self._activate_value_widget(self.value_label)

            elif field_type == bool:
                if value not in {0, 1}:
                    raise ValueError(f"Field {self.field_name} with 'bool' type has non-boolean value: {value}")
                self.value_checkbutton.var.set(value)
                self.value_checkbutton.config(fg='#3F3' if value else '#F33', text='ON' if value else 'OFF')
                self._activate_value_widget(self.value_checkbutton)

            elif field_type == list:
                # TODO: Need better display of draw groups (e.g. popout editor), as they fall off screen.
                if isinstance(value, set):
                    # Convert sets (e.g. draw/display/navmesh groups) to sorted lists so empty sets appear pretty.
                    value_text = repr(sorted(value))
                else:
                    value_text = repr(value)
                self.value_label.var.set(value_text)
                self._activate_value_widget(self.value_label)

            elif issubclass(field_type, IntEnum):
                self.value_combobox['values'] = [camel_case_to_spaces(e.name) for e in field_type]
                try:
                    # noinspection PyUnresolvedReferences
                    enum_name = camel_case_to_spaces(field_type(value).name)
                except ValueError:
                    enum_name = f"Unknown: {value}"
                self.value_combobox.var.set(enum_name)
                self._activate_value_widget(self.value_combobox)

            if self.field_links and not any(link.name for link in self.field_links) and not self.link_missing:
                self.link_missing = True
                self._update_colors()
            elif (not self.field_links or any(link.name for link in self.field_links)) and self.link_missing:
                self.link_missing = False
                self._update_colors()

            self.build_field_context_menu()
            self.tool_tip.text = docstring

            self.unhide()

        def build_field_context_menu(self):
            """For linked fields, adds an option to select an entry name from the linked table."""
            self.context_menu.delete(0, 'end')
            fg = self.STYLE_DEFAULTS['text_fg']
            if isinstance(self.field_type, str):
                for field_link in self.field_links:
                    field_link.add_to_context_menu(self.context_menu, foreground=fg)
                if self.field_type.startswith("<Maps:"):
                    self.context_menu.add_command(
                        label="Select linked entry name from list", foreground=fg,
                        command=self.choose_linked_map_entry)
                if self.field_type.startswith("<Maps:Models:Characters"):
                    self.context_menu.add_command(
                        label="Select model from complete list", foreground=fg,
                        command=self.choose_character_model)
            if self.field_type == Vector3:
                if self.field_name == "translate":
                    self.context_menu.add_command(
                        label="Copy current in-game player position", foreground=fg,
                        command=lambda: self.master.copy_player_position(translate=True, rotate=False))
                    if self.master.active_category.startswith("Regions:"):
                        self.context_menu.add_command(
                            label="Copy current in-game player position (-0.1 Y)", foreground=fg,
                            command=lambda: self.master.copy_player_position(
                                translate=True, rotate=False, y_offset=-0.1))
                elif self.field_name == "rotate":
                    self.context_menu.add_command(
                        label="Copy current in-game player rotation", foreground=fg,
                        command=lambda: self.master.copy_player_position(translate=False, rotate=True))
                if self.field_name in {"translate", "rotate"}:
                    self.context_menu.add_command(
                        label="Copy current in-game player position + rotation", foreground=fg,
                        command=lambda: self.master.copy_player_position(translate=True, rotate=True))
                    if self.master.active_category.startswith("Regions:"):
                        self.context_menu.add_command(
                            label="Copy current in-game player position (-0.1 Y) + rotation", foreground=fg,
                            command=lambda: self.master.copy_player_position(
                                translate=True, rotate=True, y_offset=-0.1))

        def choose_linked_map_entry(self):
            if not self.field_type.startswith("<Maps:"):
                return  # option shouldn't even appear
            names = self.master.linker.get_map_entry_type_names(self.field_type)  # adds suffix for Characters
            selected_name = NameSelectionBox(self.master, names).go()
            if selected_name is not None:
                selected_name = selected_name.split("  {")[0]  # remove suffix
                self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_name)
                if not self.field_links[0].name:
                    display_name = selected_name + "  {BROKEN LINK}"
                    if not self.link_missing:
                        self.link_missing = True
                        self._update_colors()
                    self.master.CustomDialog(
                        title="Map Link Error",
                        message="Map link was broken after selecting map entry from list. This should not happen; "
                                "please try restarting Soulstruct, and inform Grimrukh if the problem persists."
                    )
                else:
                    if self.field_type == "<Maps:Models:Characters|Players>":
                        model_id = int(selected_name[1:])  # ignore 'c' prefix
                        try:
                            display_name = selected_name + f"  {{{CHARACTER_MODELS[model_id]}}}"
                        except KeyError:
                            display_name = selected_name + "  {UNKNOWN}"
                    else:
                        display_name = selected_name
                    if self.link_missing:
                        self.link_missing = False
                        self._update_colors()

                self.master.change_field_value(self.field_name, selected_name)
                self.value_label.var.set(display_name)
                self.build_field_context_menu()

        def choose_character_model(self):
            if not self.field_type.startswith("<Maps:Models:Characters"):
                return  # option shouldn't even appear
            names = [f"c{model_id:04d}  {{{model_name}}}" for model_id, model_name in CHARACTER_MODELS.items()]
            selected_name = NameSelectionBox(self.master, names).go()
            if selected_name is not None:
                selected_name = selected_name.split("  {")[0]  # remove suffix
                self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_name)
                if not self.field_links[0].name:
                    self.master.add_models(self.field_type, selected_name)
                    self.field_links = self.master.linker.soulstruct_link(self.field_type, selected_name)
                if self.field_links[0].name:
                    model_id = int(selected_name[1:])  # ignore 'c' prefix
                    try:
                        display_name = selected_name + f"  {{{CHARACTER_MODELS[model_id]}}}"
                    except KeyError:
                        display_name = selected_name + "  {UNKNOWN}"
                    if self.link_missing:
                        self.link_missing = False
                        self._update_colors()
                else:
                    display_name = selected_name + "  {BROKEN LINK}"
                    if not self.link_missing:
                        self.link_missing = True
                        self._update_colors()

                self.master.change_field_value(self.field_name, selected_name)
                self.value_label.var.set(display_name)
                self.build_field_context_menu()

        @property
        def editable(self):
            return id(self.active_value_widget) in {id(self.value_label), id(self.value_vector_frame)}

        def confirm_edit(self, new_text, coord=None):
            if not self.editable:
                raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")

            if isinstance(self.field_type, str):
                # All links are integers except 'Maps' and 'MapsList'.
                if self.field_type.startswith("<MapsList:"):
                    try:
                        new_value = literal_eval(new_text)
                        if isinstance(new_value, tuple):
                            new_value = list(new_value)
                        elif not isinstance(new_value, list):
                            raise ValueError
                        if not all(i is None or isinstance(i, str) for i in new_value):
                            raise ValueError
                    except (SyntaxError, ValueError):
                        raise ValueError(
                            f"Value of field {self.field_nickname} must be a list of map entry name strings: "
                            f"['Region1', 'Region2', ... ]")
                    new_text = "(select to edit)"
                elif self.field_type.startswith("<Maps:"):
                    new_value = new_text  # map entry name
                else:
                    new_value = int(new_text)  # all other links are integer values

                self.field_links = self.master.get_field_links(self.field_type, new_value)

                if self.field_type.startswith("<MapsList:"):
                    if any(not link.name for link in self.field_links):  # at least one link is broken
                        new_text += '  {BROKEN LINK}'
                        if not self.link_missing:
                            self.link_missing = True
                            self._update_colors()
                    else:
                        # Either names are all None (no links) or all links are valid.
                        if self.link_missing:
                            self.link_missing = False
                            self._update_colors()
                elif len(self.field_links) > 1:
                    new_text += '  {AMBIGUOUS}'
                elif not self.field_links[0].name:
                    new_text += '  {BROKEN LINK}'
                    if not self.link_missing:
                        self.link_missing = True
                        self._update_colors()
                else:
                    if not self.field_type.startswith('<Maps:'):
                        new_text += f'  {{{self.field_links[0].name}}}'
                    if self.field_type == '<Maps:Models:Characters|Players>':
                        model_id = int(new_text.lstrip('c'))
                        try:
                            new_text += f'  {{{CHARACTER_MODELS[model_id]}}}'
                        except KeyError:
                            new_text += '  {UNKNOWN}'
                    if self.link_missing:
                        self.link_missing = False
                        self._update_colors()
                self.value_label.var.set(new_text)
                self.build_field_context_menu()
                return new_value

            if self.field_type in (float, Vector3):
                if new_text == "-":
                    return None  # no change
                new_value = float(new_text)
                new_text = f"{new_value:.3f}"
                if coord is not None:
                    getattr(self, f'value_vector_{coord}').var.set(f'{coord}: {new_text}')
                else:
                    self.value_label.var.set(new_text)
                return new_value
            elif self.field_type == int:
                if new_text == "-":
                    return None  # no change
                new_value = int(new_text)
                if coord is not None:
                    getattr(self, f'value_vector_{coord}').var.set(f'{coord}: {new_text}')
                else:
                    self.value_label.var.set(new_text)
                return new_value
            elif self.field_type == str:
                if coord is not None:
                    getattr(self, f'value_vector_{coord}').var.set(f'{coord}: {new_text}')
                else:
                    self.value_label.var.set(new_text)
                return new_text
            elif self.field_type == list:
                try:
                    true_value = literal_eval(new_text)
                    if isinstance(true_value, tuple):
                        true_value = list(true_value)
                    elif not isinstance(true_value, list):
                        raise ValueError
                    if not all(isinstance(i, int) for i in true_value):
                        raise ValueError
                except (SyntaxError, ValueError):
                    raise ValueError(f"Value of field {self.field_nickname} must be a list of integers: [1, 2, 3, ...]")
                if coord is not None:
                    getattr(self, f'value_vector_{coord}').var.set(f'{coord}: {new_text}')
                else:
                    self.value_label.var.set(new_text)
                return true_value
            else:
                raise TypeError(f"Could not confirm new field value of type {self.field_type}.")

        def _update_colors(self):
            bg_color = self._get_color()
            for widget in (self.row_box, self.field_name_box, self.field_name_label, self.value_box, self.value_label,
                           self.value_vector_frame, self.value_vector_x, self.value_vector_y, self.value_vector_z,
                           self.value_checkbutton):
                widget['bg'] = bg_color

    class EntryRow(SoulstructBaseFieldEditor.EntryRow):
        """Entry rows for Maps have no ID (`entry_id` is a list index in that MSB category).

        They also display their Entity ID field if they have a non-default value.
        """
        master: SoulstructMapEditor

        ENTRY_ID_WIDTH = 5
        EDIT_ENTRY_ID = False

        def __init__(self, editor: SoulstructMapEditor, row_index: int, main_bindings: dict = None):
            super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

        def update_entry(self, entry_index: int, entry_text: str, entry_description: str = ""):
            self.entry_id = entry_index
            entry_data = self.master.get_category_data()[entry_index]
            if hasattr(entry_data, "entity_id"):
                text_tail = f"  {{ID: {entry_data.entity_id}}}" if entry_data.entity_id not in {-1, 0} else ""
            elif isinstance(entry_data, MSBModel) and entry_data.ENTRY_TYPE.name in {"Character", "Player"}:
                try:
                    model_id = int(entry_text.lstrip('c'))
                except ValueError:
                    text_tail = ""
                else:
                    text_tail = f"  {{{CHARACTER_MODELS[model_id]}}}"
            else:
                text_tail = ""

            if entry_description:
                self.tool_tip.text = entry_description
            else:
                self.tool_tip.text = None
            self._entry_text = entry_text
            self.text_label.var.set(entry_text + text_tail)
            self.build_entry_context_menu()
            self.unhide()

        def build_entry_context_menu(self):
            self.context_menu.delete(0, 'end')
            self.context_menu.add_command(
                label="Edit in Floating Box (Shift + Click)", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.popout_entry_text_edit(self.row_index))
            self.context_menu.add_command(
                label="Duplicate Entry to Next Index", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.add_relative_entry(self.entry_id))
            self.context_menu.add_command(
                label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.delete_entry(self.row_index))

    entry_rows: List[SoulstructMapEditor.EntryRow]
    field_rows: List[SoulstructMapEditor.FieldRow]

    def __init__(self, maps: DarkSoulsMaps, global_map_choice_func, linker, master=None, toplevel=False):
        self.Maps = maps
        self.global_map_choice_func = global_map_choice_func
        self.e_coord = None
        self.map_choice = None
        super().__init__(linker, master=master, toplevel=toplevel, window_title="Soulstruct Map Data Editor")

    def build(self):
        with self.set_master(sticky='nsew', row_weights=[0, 1], column_weights=[1], auto_rows=0):
            with self.set_master(pady=10, sticky='w', row_weights=[1], column_weights=[1], auto_columns=0):
                map_display_names = [f"{game_map.msb_file_stem} [{game_map.verbose_name}]"
                                     for game_map in ALL_MAPS if game_map.msb_file_stem]
                self.map_choice = self.Combobox(
                    values=map_display_names, label='Map:', label_font_size=12, label_position='left', width=35,
                    font=('Segoe UI', 12), on_select_function=self.on_map_choice, sticky='w', padx=10)

            super().build()

    def refresh_entries(self, reset_field_display=False):
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()

        entries_to_display = self._get_category_name_range(
            first_index=self.first_display_index,
            last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
        )

        row = 0
        for entry_id, _ in entries_to_display:
            self.entry_rows[row].update_entry(entry_id, self.get_entry_text(entry_id),
                                              self.get_entry_description(entry_id))
            self.entry_rows[row].unhide()
            row += 1

        self.displayed_entry_count = row
        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            self.entry_rows[remaining_row].hide()

        self.entry_i_frame.columnconfigure(0, weight=1)
        self.entry_i_frame.columnconfigure(1, weight=1)
        if self.displayed_entry_count == 0:
            self.select_entry_row_index(None)
        self._refresh_range_buttons()

        self.refresh_fields(reset_display=reset_field_display)

    def on_map_choice(self, event=None):
        if self.global_map_choice_func and event is not None:
            self.global_map_choice_func(self.map_choice_id, ignore_tabs=("maps",))
        self.select_entry_row_index(None)
        self.refresh_entries(reset_field_display=True)

    @staticmethod
    def _get_category_text_fg(category: str):
        return ENTRY_LIST_FG_COLORS.get(category.split(':')[0], '#FFF')

    def _add_entry(self, entry_type_index: int, text: str, category=None, new_field_dict: MSBEntry = None):
        """Active category is required."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("Cannot add entry without specifying category if 'active_category' is None.")
        entry_list_name, entry_type_name = category.split(': ')
        entry_list = self.get_selected_msb()[entry_list_name]
        global_index = entry_list.get_entry_global_index(entry_type_index, entry_type=entry_type_name)
        if global_index is None:
            global_index = len(entry_list)  # appending to end locally -> appending to end globally

        if not 0 <= global_index <= len(entry_list):
            self.CustomDialog(
                title="Entry Index Error",
                message=f"Entry index must be between zero and the current list length.")
            return False

        self._cancel_entry_text_edit()
        new_field_dict.name = text
        entry_list.add_entry(new_field_dict, global_index)
        local_index = entry_list.get_entries(entry_type=new_field_dict.ENTRY_TYPE).index(new_field_dict)
        self.select_entry_id(local_index, set_focus_to_text=True, edit_if_already_selected=False)
        # TODO: ActionHistory stuff?
        return True

    def add_relative_entry(self, entry_index, offset=1, text=None):
        """Uses entry index instead of dictionary ID."""
        if text is None:
            text = self.get_entry_text(entry_index)  # Copies name of origin entry by default.
        new_field_dict = self.get_category_data()[entry_index].copy()
        return self._add_entry(entry_index + offset, text, new_field_dict=new_field_dict)

    def delete_entry(self, row_index, category=None):
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("Cannot delete entry without specifying category if 'active_category' is None.")
        self._cancel_entry_text_edit()
        entry_type_index = self.get_entry_id(row_index)

        entry_list_name, entry_type_name = category.split(': ')
        entry_list = self.get_selected_msb()[entry_list_name]
        global_index = entry_list.get_entry_global_index(entry_type_index, entry_type=entry_type_name)
        if global_index is None:
            raise IndexError(f"Cannot delete entry with global index {global_index} (list length is {len(entry_list)}.")
        entry_list.delete_entry(global_index)
        self.select_entry_row_index(None)
        self.refresh_entries()

    def popout_entry_text_edit(self, row_index):
        """Can actually change both ID and text."""
        entry_id = self.get_entry_id(row_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = self.get_entry_text(entry_id, self.active_category)
            popout_editor = EntryTextEditBox(self, self.active_category, category_data=self.get_category_data(),
                                             entry_id=entry_id, initial_text=initial_text, edit_entry_id=False)
            try:
                _, new_text = popout_editor.go()
            except Exception as e:
                _LOGGER.error(e, exc_info=True)
                return self.CustomDialog(
                    "Entry Text Error", f"Error occurred while setting entry text:\n\n{e}")
            if new_text is not None:
                self.change_entry_text(row_index, new_text)

    def select_displayed_field_row(self, row_index, set_focus_to_value=True, edit_if_already_selected=True, coord=None):
        old_row_index = self.selected_field_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected and self.field_rows[row_index].editable:
                    return self._start_field_value_edit(row_index, coord=coord)
                return
        else:
            self._cancel_field_value_edit()

        self.selected_field_row_index = row_index

        if old_row_index is not None:
            self.field_rows[old_row_index].active = False
        if row_index is not None:
            self.field_rows[row_index].active = True
            if set_focus_to_value:
                self.field_rows[row_index].active_value_widget.focus_set()

    # TODO: how does field_press react if a coord is being edited? Should go to next coord, probably.

    def _get_field_edit_widget(self, row_index):
        field_row = self.field_rows[row_index]
        if not field_row.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
        field_type = field_row.field_type
        field_value = self.get_field_dict(self.get_entry_id(self.active_row_index))[field_row.field_name]
        if field_type in {int, float, str, list} or isinstance(field_type, str):
            return self.Entry(
                field_row.value_box,
                initial_text=str(field_value),
                numbers_only=field_type == float,
                integers_only=field_type == int,
                sticky='ew', width=5)
        elif field_type == Vector3:
            if self.e_coord is None:
                return None  # Exact coordinate not clicked.
            return self.Entry(
                field_row.value_vector_frame, initial_text=getattr(field_value, self.e_coord),
                numbers_only=True, sticky='ew', width=5, column='xyz'.index(self.e_coord))
        raise TypeError(f"Could not determine editing box from type {field_type}.")

    def _start_field_value_edit(self, row_index, coord=None):
        if self.e_field_value_edit and self.e_coord and coord and coord != self.e_coord:
            # Finish up previous coord edit.
            self._confirm_field_value_edit(row_index)
        self.e_coord = coord
        super()._start_field_value_edit(row_index)

    def _cancel_field_value_edit(self):
        if self.e_field_value_edit:
            self.e_field_value_edit.destroy()
            self.e_field_value_edit = None
            self.e_coord = None

    def _confirm_field_value_edit(self, row_index):
        if self.e_field_value_edit:
            row = self.field_rows[row_index]
            try:
                true_value = row.confirm_edit(new_text=self.e_field_value_edit.var.get(), coord=self.e_coord)
            except ValueError as e:
                # Entry input restrictions will usually prevent this.
                _LOGGER.error(f"Invalid field value. Error: {str(e)}")
                self.bell()
                self.CustomDialog("Invalid Field Value", f"Invalid field value. Error:\n\n{str(e)}")
                return
            self.change_field_value(row.field_name, true_value)
            self._cancel_field_value_edit()

            if (isinstance(row.field_type, str) and row.field_type.startswith("<Maps:Models:")
                    and row.field_links[0].name is None):
                # Offer to create models (after checking if they're valid).
                if self.add_models(row.field_type, true_value):
                    row.confirm_edit(true_value)  # Refresh links.

    def change_field_value(self, field_name: str, new_value):
        field_dict = self.get_selected_field_dict()
        old_value = field_dict[field_name]
        if self.e_coord:
            old_value = getattr(old_value, self.e_coord)
        if old_value == new_value:
            return False  # Nothing to change.
        try:
            if self.e_coord:
                setattr(field_dict[field_name], self.e_coord, new_value)
            else:
                field_dict[field_name] = new_value
        except InvalidFieldValueError as e:
            self.bell()
            self.CustomDialog(title="Field Value Error", message=str(e))
            return False
        return True

    def _field_press_up(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new_row = self.e_field_value_edit is not None
            new_coord = ""
            if self.e_coord is not None:
                if self.e_coord == "y":
                    new_coord = "x"
                    edit_new_row = False
                elif self.e_coord == "z":
                    new_coord = "y"
                    edit_new_row = False
            self._confirm_field_value_edit(self.selected_field_row_index)
            if new_coord in {"x", "y"}:
                self._start_field_value_edit(self.selected_field_row_index, coord=new_coord)
            else:
                self._shift_selected_field(-1)
            if edit_new_row and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[1] != 1.0 or self.selected_field_row_index < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, 'units')

    def _field_press_down(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new_row = self.e_field_value_edit is not None or self.e_coord
            new_coord = ""
            if self.e_coord is not None:
                if self.e_coord == "x":
                    new_coord = "y"
                    edit_new_row = False
                elif self.e_coord == "y":
                    new_coord = "z"
                    edit_new_row = False
            self._confirm_field_value_edit(self.selected_field_row_index)
            if new_coord in {"y", "z"}:
                self._start_field_value_edit(self.selected_field_row_index, coord=new_coord)
            else:
                self._shift_selected_field(+1)
            if edit_new_row and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[0] != 0.0 or self.selected_field_row_index > 5:
                self.field_canvas.yview_scroll(1, 'units')

    def _get_display_categories(self):
        """ALl combinations of MSB entry list names and their subtypes, properly formatted."""
        categories = []
        for entry_list_name, entry_type_names in MAP_ENTRY_TYPES.items():
            for name in entry_type_names:
                if name in {"Circles", "Rectangles"}:
                    continue  # These useless region types are hidden.
                categories.append(f'{entry_list_name}: {name}')
        return categories

    def get_selected_msb(self):
        map_name = get_map(self.map_choice_id).name
        return self.Maps[map_name]

    def get_category_data(self, category=None) -> List[MSBEntry]:
        """Gets entry data from map choice, entry list choice, and entry type choice (active category).

        For Maps, this actually returns a *list*, not a dict. Entry IDs are equivalent to entry indexes in this list, so
        all parent methods still function as expected.
        """
        if category is None:
            category = self.active_category
            if category is None:
                return []
        selected_msb = self.get_selected_msb()
        try:
            entry_list, entry_type = category.split(': ')
        except ValueError:
            raise ValueError(f"Category name was not in [List: Type] format: {category}")
        return selected_msb[entry_list].get_entries(entry_type)

    def _get_category_name_range(self, category=None, first_index=None, last_index=None):
        """Returns a zip() generator for parent method."""
        entry_list = self.get_category_data(category)
        return zip(range(first_index, last_index), entry_list[first_index:last_index])

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Entry index and entry ID are equivalent in Maps.

        Note that .get_entry_id() is still necessary to get the true entry index from the displayed row index.
        """
        return entry_id

    def get_entry_text(self, entry_index: int, category=None) -> str:
        entry_list = self.get_category_data(category)
        return entry_list[entry_index].name

    def get_entry_description(self, entry_index: int, category=None) -> str:
        entry_list = self.get_category_data(category)
        return entry_list[entry_index].description

    def _set_entry_text(self, entry_index: int, text: str, category=None, update_row_index=None):
        entry_list = self.get_category_data(category)
        entry_list[entry_index].name = text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_index, text, entry_list[entry_index].description)

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        """Not implemented for Map Editor."""
        raise NotImplementedError

    def get_field_dict(self, entry_index: int, category=None) -> MSBEntry:
        """Uses entry index instad of entry ID."""
        return self.get_category_data(category)[entry_index]

    def get_field_info(self, field_dict, field_name=None):
        if field_dict is None:
            return {}
        if field_name is not None:
            return field_dict.FIELD_INFO[field_name]
        return field_dict.FIELD_INFO

    def get_field_names(self, field_dict):
        return field_dict.field_names if field_dict else []

    def get_field_links(self, field_type, field_value, valid_null_values=None) -> list:
        if valid_null_values is None:
            if field_type == '<Text:PlaceNames>':
                valid_null_values = {-1: 'Default Map Name + Force Banner'}
            else:
                valid_null_values = {0: 'Default/None', -1: 'Default/None'}
        return self.linker.soulstruct_link(field_type, field_value, valid_null_values=valid_null_values)

    def add_models(self, model_link, model_name):
        if model_link == "<Maps:Models:Characters|Players>":
            model_type = "Characters"
        else:
            model_type = re.match(r"<Maps:Models:(\w+)>", model_link).group(1)

        map_id = self.map_choice_id
        if self.linker.validate_model_type(model_type, model_name, map_id=map_id):
            if self.CustomDialog(
                    title=f"Add {model_type} Model",
                    message=f"Add {model_type} model {model_name} to map?",
                    button_names=("Yes, add it", "No, leave as missing"),
                    button_kwargs=("YES", "NO"),
                    return_output=0, default_output=0, cancel_output=1
            ) == 0:
                if model_type in {"MapPieces", "Collisions", "Navmeshes"}:
                    sib_path = (int(map_id[1:3]), int(map_id[4:6]))
                else:
                    sib_path = None  # fine for Objects, Characters, and Players
                new_model = MSBModel(name=model_name, entry_type=model_type, sib_path=sib_path)
                self.get_selected_msb().models.add_entry(new_model, append_to_entry_type=model_type)
                return True
        else:
            self.CustomDialog(
                title=f"Invalid {model_type} Model",
                message=f"{model_type} model {model_name} does not have any data in the game files.\n"
                        f"This will likely cause severe problems in your game!",
            )

        return False

    def copy_player_position(self, translate=False, rotate=False, y_offset=0.0):
        if not translate and not rotate:
            raise ValueError("At least one of `translate` and `rotate` should be True.")
        new_translate = None
        new_rotate_y = None
        try:
            if translate:
                player_x = self.linker.get_game_value("player_x")
                player_y = self.linker.get_game_value("player_y") + y_offset
                player_z = self.linker.get_game_value("player_z")
                new_translate = Vector3(player_x, player_y, player_z)
            if rotate:
                new_rotate_y = math.degrees(self.linker.get_game_value("player_angle"))
        except ConnectionError:
            if self.CustomDialog(
                    title="Cannot Read Memory",
                    message="Runtime hooks are not available. Would you like to try hooking into the game now?",
                    default_output=0, cancel_output=1, return_output=0,
                    button_names=("Yes, hook in", "No, forget it"),
                    button_kwargs=("YES", "NO"),
            ) == 1:
                return
            if self.linker.runtime_hook():
                return self.copy_player_position(translate=translate, rotate=rotate, y_offset=y_offset)
            return
        except MemoryHookError as e:
            _LOGGER.error(str(e), exc_info=True)
            self.CustomDialog(
                title="Cannot Read Memory",
                message=f"An error occurred when trying to copy player position (see log for full traceback):\n\n"
                        f"{str(e)}\n\n"
                        f"If this error doesn't seem like it can be solved (e.g. did you close the game after\n"
                        f"hooking into it?) please inform Grimrukh.")
            return
        field_dict = self.get_selected_field_dict()
        if translate:
            field_dict["translate"] = new_translate
        if rotate:
            field_dict["rotate"].y = new_rotate_y
        self.refresh_fields()
