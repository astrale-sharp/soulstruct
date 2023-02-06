from __future__ import annotations

__all__ = ["BaseMSBPart"]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.maths import Vector3

from .models import BaseMSBModel
from .msb_entry import MSBEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "BaseMSBPart"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class BaseMSBPart(MSBEntry, abc.ABC):

    # Number of bits in draw/display/navmesh/backread groups (e.g. 128 or 256).
    GROUP_SIZE: tp.ClassVar[int]

    model: BaseMSBModel = ""
    entity_id: int = -1
    translate: Vector3 = field(default_factory=lambda: Vector3.zero())
    rotate: Vector3 = field(default_factory=lambda: Vector3.zero())
    scale: Vector3 = field(default_factory=lambda: Vector3.zero())

    draw_parent: BaseMSBPart | None = None
    draw_groups: set[int] = field(default_factory=set)
    display_groups: set[int] = field(default_factory=set)

    _model_index: int = -1
    _draw_parent_index: int = -1

    # Game structures diverge too much for useful read/write base methods here.

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        """Defined by most subclasses."""
        self._consume_index(entry_lists, "parts", "model")
        self._consume_index(entry_lists, "parts", "draw_parent")
