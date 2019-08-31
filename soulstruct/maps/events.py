from io import BufferedReader, BytesIO
from enum import IntEnum
import struct

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, Vector


class MSB_EVENT_TYPE(IntEnum):
    Light = 0
    Sound = 1
    FX = 2
    Wind = 3
    Treasure = 4
    Spawner = 5
    Message = 6
    ObjAct = 7
    SpawnPoint = 8
    MapOffset = 9
    Navmesh = 10
    Environment = 11
    NPCInvasion = 12


def MSBEvent(msb_buffer):
    """Detects the appropriate subclass of BaseMSBEvent to instantiate."""
    # TODO: support more types?
    return BaseMSBEvent.auto_event_subclass(msb_buffer)


class BaseMSBEvent(object):
    EVENT_HEADER_STRUCT = BinaryStruct(
        ('name_offset', 'i'),
        ('event_index', 'i'),
        ('event_type', 'I'),
        ('event_type_index', 'i'),
        ('base_data_offset', 'i'),
        ('type_data_offset', 'i'),
        '4x',
    )
    # Name is stored next.
    # Base data is stored next.
    # Type data is stored next.

    EVENT_BASE_DATA_STRUCT = BinaryStruct(
        ('part_index', 'i'),
        ('region_index', 'i'),
        ('entity_id', 'i'),
        '4x',
    )

    EVENT_TYPE = -1

    def __init__(self, msb_event_source):
        self.name = ''
        self._event_index = None  # global index
        self._event_type_index = None  # local type index
        self.entity_id = None
        self.base_part_name = None
        self._base_part_index = None
        self.base_region_name = None
        self._base_region_index = None

        if isinstance(msb_event_source, bytes):
            msb_event_source = BytesIO(msb_event_source)
        if isinstance(msb_event_source, BufferedReader):
            self.unpack(msb_event_source)
        else:
            raise TypeError("'msb_event_source' must be a buffer or bytes.")

    def unpack_base(self, msb_buffer):
        event_offset = msb_buffer.tell()
        header = self.EVENT_HEADER_STRUCT.unpack(msb_buffer)
        if header.event_type != self.EVENT_TYPE:
            raise ValueError(f"Unexpected event type enum {header.event_type} for class {self.__class__.__name__}.")

        msb_buffer.seek(event_offset + header.base_data_offset)
        base_data = self.EVENT_BASE_DATA_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(msb_buffer, offset=event_offset + header.name_offset, encoding='shift-jis')
        self._event_index = header.event_index
        self._event_type_index = header.event_type_index
        self._base_part_index = base_data.part_index
        self._base_region_index = base_data.region_index
        self.entity_id = base_data.entity_id
        msb_buffer.seek(event_offset + header.type_data_offset)

    def set_indices(self, event_index, event_type_index, region_indices, part_indices):
        self._event_index = event_index
        self._event_type_index = event_type_index
        self._base_part_index = part_indices[self.base_part_name] if self.base_part_name else -1
        self._base_region_index = region_indices[self.base_region_name] if self.base_region_name else -1

    def set_names(self, region_names, part_names):
        self.base_part_name = part_names[self._base_part_index] if self._base_part_index != -1 else None
        self.base_region_name = region_names[self._base_region_index] if self._base_region_index != -1 else None

    def unpack(self, msb_buffer):
        raise NotImplementedError

    def pack(self):
        name_offset = self.EVENT_HEADER_STRUCT.size
        packed_name = self.name.encode('shift-jis')
        while len(packed_name) % 4 != 0:
            packed_name += b'\0'
        base_data_offset = name_offset + len(packed_name)
        packed_base_data = self.EVENT_BASE_DATA_STRUCT.pack(
            part_index=self._base_part_index,
            region_index=self._base_region_index,
            entity_id=self.entity_id,
        )
        type_data_offset = base_data_offset + len(packed_base_data)
        packed_type_data = self.pack_type_data()
        packed_header = self.EVENT_HEADER_STRUCT.pack(
            name_offset=name_offset,
            event_index=self._event_index,
            event_type=self.EVENT_TYPE,
            event_type_index=self._event_type_index,
            base_data_offset=base_data_offset,
            type_data_offset=type_data_offset,
        )
        return packed_header + packed_name + packed_base_data + packed_type_data

    def pack_type_data(self):
        raise NotImplementedError

    @staticmethod
    def auto_event_subclass(msb_buffer):
        old_offset = msb_buffer.tell()
        msb_buffer.seek(old_offset + 8)
        try:
            event_type_int = struct.unpack('i', msb_buffer.read(4))[0]
            event_type = MSB_EVENT_TYPE(event_type_int)
        except (ValueError, TypeError):
            event_type = None
        msb_buffer.seek(old_offset)
        return MSB_EVENT_TYPE_CLASSES[event_type](msb_buffer)


class MSBLight(BaseMSBEvent):
    EVENT_LIGHT_STRUCT = (
        ('unk_x00_x04', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Light

    def __init__(self, msb_event_source):
        self.unk_x00_x04 = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_LIGHT_STRUCT).unpack(msb_buffer)
        self.unk_x00_x04 = data.unk_x00_x04

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_LIGHT_STRUCT).pack(
            unk_x00_x04=self.unk_x00_x04,
        )


class MSBSound(BaseMSBEvent):
    EVENT_SOUND_STRUCT = (
        ('sound_type', 'i'),
        ('sound_id', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Sound

    def __init__(self, msb_event_source):
        self.sound_type = None
        self.sound_id = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_SOUND_STRUCT).unpack(msb_buffer)
        self.sound_type = data.sound_type
        self.sound_id = data.sound_id

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_SOUND_STRUCT).pack(
            sound_type=self.sound_type,
            sound_id=self.sound_id,
        )


class MSBFX(BaseMSBEvent):
    EVENT_FX_STRUCT = (
        ('fx_id', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.FX

    def __init__(self, msb_event_source):
        self.fx_id = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_FX_STRUCT).unpack(msb_buffer)
        self.fx_id = data.fx_id

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_FX_STRUCT).pack(
            fx_id=self.fx_id,
        )


class MSBWind(BaseMSBEvent):
    EVENT_WIND_STRUCT = (
        ('unk_x00_x04', 'f'),
        ('unk_x04_x08', 'f'),
        ('unk_x08_x0c', 'f'),
        ('unk_x0c_x10', 'f'),
        ('unk_x10_x14', 'f'),
        ('unk_x14_x18', 'f'),
        ('unk_x18_x1c', 'f'),
        ('unk_x1c_x20', 'f'),
        ('unk_x20_x24', 'f'),
        ('unk_x24_x28', 'f'),
        ('unk_x28_x2c', 'f'),
        ('unk_x2c_x30', 'f'),
        ('unk_x30_x34', 'f'),
        ('unk_x34_x38', 'f'),
        ('unk_x38_x3c', 'f'),
        ('unk_x3c_x40', 'f'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Wind

    def __init__(self, msb_event_source):
        """Data consists of 16 floats, which likely specify the transform parameters (e.g. position, direction) of wind
        effects in the map."""
        self.unk_x00_x04 = None
        self.unk_x04_x08 = None
        self.unk_x08_x0c = None
        self.unk_x0c_x10 = None
        self.unk_x10_x14 = None
        self.unk_x14_x18 = None
        self.unk_x18_x1c = None
        self.unk_x1c_x20 = None
        self.unk_x20_x24 = None
        self.unk_x24_x28 = None
        self.unk_x28_x2c = None
        self.unk_x2c_x30 = None
        self.unk_x30_x34 = None
        self.unk_x34_x38 = None
        self.unk_x38_x3c = None
        self.unk_x3c_x40 = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_WIND_STRUCT).unpack(msb_buffer)
        self.unk_x00_x04 = data.unk_x00_x04
        self.unk_x04_x08 = data.unk_x04_x08
        self.unk_x08_x0c = data.unk_x08_x0c
        self.unk_x0c_x10 = data.unk_x0c_x10
        self.unk_x10_x14 = data.unk_x10_x14
        self.unk_x14_x18 = data.unk_x14_x18
        self.unk_x18_x1c = data.unk_x18_x1c
        self.unk_x1c_x20 = data.unk_x1c_x20
        self.unk_x20_x24 = data.unk_x20_x24
        self.unk_x24_x28 = data.unk_x24_x28
        self.unk_x28_x2c = data.unk_x28_x2c
        self.unk_x2c_x30 = data.unk_x2c_x30
        self.unk_x30_x34 = data.unk_x30_x34
        self.unk_x34_x38 = data.unk_x34_x38
        self.unk_x38_x3c = data.unk_x38_x3c
        self.unk_x3c_x40 = data.unk_x3c_x40

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_WIND_STRUCT).pack(
            unk_x00_x04=self.unk_x00_x04,
            unk_x04_x08=self.unk_x04_x08,
            unk_x08_x0c=self.unk_x08_x0c,
            unk_x0c_x10=self.unk_x0c_x10,
            unk_x10_x14=self.unk_x10_x14,
            unk_x14_x18=self.unk_x14_x18,
            unk_x18_x1c=self.unk_x18_x1c,
            unk_x1c_x20=self.unk_x1c_x20,
            unk_x20_x24=self.unk_x20_x24,
            unk_x24_x28=self.unk_x24_x28,
            unk_x28_x2c=self.unk_x28_x2c,
            unk_x2c_x30=self.unk_x2c_x30,
            unk_x30_x34=self.unk_x30_x34,
            unk_x34_x38=self.unk_x34_x38,
            unk_x38_x3c=self.unk_x38_x3c,
            unk_x3c_x40=self.unk_x3c_x40,
        )


class MSBTreasure(BaseMSBEvent):
    EVENT_TREASURE_STRUCT = (
        '4x',
        ('treasure_part_index', 'i'),
        ('item_lot_1', 'i'),
        ('minus_one_1', 'i', -1),
        ('item_lot_2', 'i'),
        ('minus_one_2', 'i', -1),
        ('item_lot_3', 'i'),
        ('minus_one_3', 'i', -1),
        ('item_lot_4', 'i'),
        ('minus_one_4', 'i', -1),
        ('item_lot_5', 'i'),
        ('minus_one_5', 'i', -1),
        ('in_chest', '?'),
        ('start_disabled', '?'),
        '2x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Treasure

    def __init__(self, msb_event_source):
        self.treasure_part_name = None
        self._treasure_part_index = None
        self.item_lot_1 = None
        self.item_lot_2 = None
        self.item_lot_3 = None
        self.item_lot_4 = None
        self.item_lot_5 = None
        self.in_chest = None
        self.start_disabled = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_TREASURE_STRUCT).unpack(msb_buffer)
        self._treasure_part_index = data.treasure_part_index
        self.item_lot_1 = data.item_lot_1
        self.item_lot_2 = data.item_lot_2
        self.item_lot_3 = data.item_lot_3
        self.item_lot_4 = data.item_lot_4
        self.item_lot_5 = data.item_lot_5
        self.in_chest = data.in_chest
        self.start_disabled = data.start_disabled

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_TREASURE_STRUCT).pack(
            treasure_part_index=self._treasure_part_index,
            item_lot_1=self.item_lot_1,
            item_lot_2=self.item_lot_2,
            item_lot_3=self.item_lot_3,
            item_lot_4=self.item_lot_4,
            item_lot_5=self.item_lot_5,
            in_chest=self.in_chest,
            start_disabled=self.start_disabled,
        )

    def set_indices(self, event_index, event_type_index, region_indices, part_indices):
        super().set_indices(event_index, event_type_index, region_indices, part_indices)
        self._treasure_part_index = part_indices[self.treasure_part_name] if self.treasure_part_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.treasure_part_name = part_names[self._treasure_part_index] if self._treasure_part_index != -1 else None


class MSBSpawner(BaseMSBEvent):
    EVENT_SPAWNER_STRUCT = (
        ('max_count', 'h'),
        ('limit_count', 'h'),
        ('min_spawner_count', 'h'),
        ('max_spawner_count', 'h'),
        ('min_interval', 'f'),
        ('max_interval', 'f'),
        ('initial_spawn_count', 'i'),
        '28x',
        ('spawn_region_indices', '4i'),
        ('spawn_part_indices', '32i'),
        '64x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Spawner

    def __init__(self, msb_event_source):
        self.max_count = None
        self.limit_count = None
        self.min_spawner_count = None
        self.max_spawner_count = None
        self.min_interval = None
        self.max_interval = None
        self.initial_spawn_count = None
        self.spawn_region_names = None
        self._spawn_region_indices = None
        self.spawn_part_names = None
        self._spawn_part_indices = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_SPAWNER_STRUCT).unpack(msb_buffer)
        self.max_count = data.max_count
        self.limit_count = data.limit_count
        self.min_spawner_count = data.min_spawner_count
        self.max_spawner_count = data.max_spawner_count
        self.min_interval = data.min_interval
        self.max_interval = data.max_interval
        self.initial_spawn_count = data.initial_spawn_count
        self._spawn_region_indices = data.spawn_region_indices
        self._spawn_part_indices = data.spawn_part_indices

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_SPAWNER_STRUCT).pack(
            max_count=self.max_count,
            limit_count=self.limit_count,
            min_spawner_count=self.min_spawner_count,
            max_spawner_count=self.max_spawner_count,
            min_interval=self.min_interval,
            max_interval=self.max_interval,
            initial_spawn_count=self.initial_spawn_count,
            spawn_region_indices=self._spawn_region_indices,
            spawn_part_indicies=self._spawn_part_indices,
        )

    def set_indices(self, event_index, event_type_index, region_indices, part_indices):
        super().set_indices(event_index, event_type_index, region_indices, part_indices)
        self._spawn_part_indices = [part_indices[n] if n else -1 for n in self.spawn_part_names]
        self._spawn_region_indices = [region_indices[n] if n else -1 for n in self.spawn_region_names]

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.spawn_part_names = [part_names[i] if i != -1 else None for i in self._spawn_part_indices]
        self.spawn_region_names = [region_names[i] if i != -1 else None for i in self._spawn_region_indices]


class MSBMessage(BaseMSBEvent):
    EVENT_MESSAGE_STRUCT = (
        ('text_id', 'h'),
        ('unk_x02_x04', 'h'),
        ('is_hidden', '?'),
        '3x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Message

    def __init__(self, msb_event_source):
        self.text_id = None
        self.unk_x02_x04 = None
        self.is_hidden = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_MESSAGE_STRUCT).unpack(msb_buffer)
        self.text_id = data.text_id
        self.unk_x02_x04 = data.unk_x02_x04
        self.is_hidden = data.is_hidden

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_MESSAGE_STRUCT).pack(
            text_id=self.text_id,
            unk_x02_x04=self.unk_x02_x04,
            is_hidden=self.is_hidden,
        )


class MSBObjAct(BaseMSBEvent):
    EVENT_OBJ_ACT_STRUCT = (
        ('obj_act_entity_id', 'i'),
        ('obj_act_part_index', 'i'),
        ('obj_act_param_id', 'h'),
        ('unk_x0a_x0c', 'h'),
        ('obj_act_flag', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.ObjAct

    def __init__(self, msb_event_source):
        self.obj_act_entity_id = None
        self.obj_act_part_name = None
        self._obj_act_part_index = None
        self.obj_act_param_id = None
        self.unk_x0a_x0c = None
        self.obj_act_flag = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_OBJ_ACT_STRUCT).unpack(msb_buffer)
        self.obj_act_entity_id = data.obj_act_entity_id
        self._obj_act_part_index = data.obj_act_part_index
        self.obj_act_param_id = data.obj_act_param_id
        self.unk_x0a_x0c = data.unk_x0a_x0c
        self.obj_act_flag = data.obj_act_flag

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_OBJ_ACT_STRUCT).pack(
            obj_act_entity_id=self.obj_act_entity_id,
            obj_act_part_index=self._obj_act_part_index,
            obj_act_param_id=self.obj_act_param_id,
            unk_x0a_x0c=self.unk_x0a_x0c,
            obj_act_flag=self.obj_act_flag,
        )

    def set_indices(self, event_index, event_type_index, region_indices, part_indices):
        super().set_indices(event_index, event_type_index, region_indices, part_indices)
        self._obj_act_part_index = part_indices[self.obj_act_part_name] if self.obj_act_part_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.obj_act_part_name = part_names[self._obj_act_part_index] if self._obj_act_part_index != -1 else None


class MSBSpawnPoint(BaseMSBEvent):
    EVENT_SPAWN_POINT_STRUCT = (
        ('spawn_point_region_index', 'i'),
        '12x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.SpawnPoint

    def __init__(self, msb_event_source):
        self.spawn_point_region_name = None
        self._spawn_point_region_index = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_SPAWN_POINT_STRUCT).unpack(msb_buffer)
        self._spawn_point_region_index = data.spawn_point_region_index

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_SPAWN_POINT_STRUCT).pack(
            spawn_point_region_index=self._spawn_point_region_index,
        )

    def set_indices(self, event_index, event_type_index, region_indices, part_indices):
        super().set_indices(event_index, event_type_index, region_indices, part_indices)
        if self.spawn_point_region_name:
            self._spawn_point_region_index = region_indices[self.spawn_point_region_name]
        else:
            self._spawn_point_region_index = -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        if self._spawn_point_region_index != -1:
            self.spawn_point_region_name = region_names[self._spawn_point_region_index]
        else:
            self.spawn_point_region_name = None


class MSBMapOffset(BaseMSBEvent):
    EVENT_MAP_OFFSET_STRUCT = (
        ('translate_x', 'f'),
        ('translate_y', 'f'),
        ('translate_z', 'f'),
        ('rotate_y', 'f'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.MapOffset

    def __init__(self, msb_event_source):
        self.translate = None
        self.rotate_y = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_MAP_OFFSET_STRUCT).unpack(msb_buffer)
        self.translate = Vector(data.translate_x, data.translate_y, data.translate_z)
        self.rotate_y = data.rotate_y

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_MAP_OFFSET_STRUCT).pack(
            translate_x=self.translate.x,
            translate_y=self.translate.y,
            translate_z=self.translate.z,
            rotate_y=self.rotate_y,
        )


class MSBNavmesh(BaseMSBEvent):
    EVENT_NAVMESH_STRUCT = (
        ('navmesh_region_index', 'i'),
        '12x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Navmesh

    def __init__(self, msb_event_source):
        self.navmesh_region_name = None
        self._navmesh_region_index = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_NAVMESH_STRUCT).unpack(msb_buffer)
        self._navmesh_region_index = data.navmesh_region_index

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_NAVMESH_STRUCT).pack(
            navmesh_region_index=self._navmesh_region_index,
        )

    def set_indices(self, event_index, event_type_index, region_indices, part_indices):
        super().set_indices(event_index, event_type_index, region_indices, part_indices)
        self._navmesh_region_index = region_indices[self.navmesh_region_name] if self.navmesh_region_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        if self._navmesh_region_index != -1:
            self.navmesh_region_name = region_names[self._navmesh_region_index]
        else:
            self.navmesh_region_name = None


class MSBEnvironment(BaseMSBEvent):
    EVENT_ENVIRONMENT_STRUCT = (
        ('unk_x00_x04', 'i'),
        ('unk_x04_x08', 'f'),
        ('unk_x08_x0c', 'f'),
        ('unk_x0c_x10', 'f'),
        ('unk_x10_x14', 'f'),
        ('unk_x14_x18', 'f'),
        '8x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Environment

    def __init__(self, msb_event_source):
        self.unk_x00_x04 = None
        self.unk_x04_x08 = None
        self.unk_x08_x0c = None
        self.unk_x0c_x10 = None
        self.unk_x10_x14 = None
        self.unk_x14_x18 = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_ENVIRONMENT_STRUCT).unpack(msb_buffer)
        self.unk_x00_x04 = data.unk_x00_x04
        self.unk_x04_x08 = data.unk_x04_x08
        self.unk_x08_x0c = data.unk_x08_x0c
        self.unk_x0c_x10 = data.unk_x0c_x10
        self.unk_x10_x14 = data.unk_x10_x14
        self.unk_x14_x18 = data.unk_x14_x18

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_ENVIRONMENT_STRUCT).pack(
            unk_x00_x04=self.unk_x00_x04,
            unk_x04_x08=self.unk_x04_x08,
            unk_x08_x0c=self.unk_x08_x0c,
            unk_x0c_x10=self.unk_x0c_x10,
            unk_x10_x14=self.unk_x10_x14,
            unk_x14_x18=self.unk_x14_x18,
        )


class MSBNPCInvasion(BaseMSBEvent):
    EVENT_NPC_INVASION_STRUCT = (
        ('host_entity_id', 'i'),
        ('invasion_flag_id', 'i'),
        ('spawn_point_region_index', 'i'),
        '4x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.NPCInvasion

    def __init__(self, msb_event_source):
        self.host_entity_id = None
        self.invasion_flag_id = None
        self.spawn_point_region_name = None
        self._spawn_point_region_index = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_NPC_INVASION_STRUCT).unpack(msb_buffer)
        self.host_entity_id = data.host_entity_id
        self.invasion_flag_id = data.invasion_flag_id
        self._spawn_point_region_index = data.spawn_point_region_index

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_NPC_INVASION_STRUCT).pack(
            host_entity_id=self.host_entity_id,
            invasion_flag_id=self.invasion_flag_id,
            spawn_point_region_index=self._spawn_point_region_index,
        )

    def set_indices(self, event_index, event_type_index, region_indices, part_indices):
        super().set_indices(event_index, event_type_index, region_indices, part_indices)
        if self.spawn_point_region_name:
            self._spawn_point_region_index = region_indices[self.spawn_point_region_name]
        else:
            self._spawn_point_region_index = -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        if self._spawn_point_region_index != -1:
            self.spawn_point_region_name = region_names[self._spawn_point_region_index]
        else:
            self.spawn_point_region_name = None


MSB_EVENT_TYPE_CLASSES = {
    MSB_EVENT_TYPE.Light: MSBLight,
    MSB_EVENT_TYPE.Sound: MSBSound,
    MSB_EVENT_TYPE.FX: MSBFX,
    MSB_EVENT_TYPE.Wind: MSBWind,
    MSB_EVENT_TYPE.Treasure: MSBTreasure,
    MSB_EVENT_TYPE.Spawner: MSBSpawner,
    MSB_EVENT_TYPE.Message: MSBMessage,
    MSB_EVENT_TYPE.ObjAct: MSBObjAct,
    MSB_EVENT_TYPE.SpawnPoint: MSBSpawnPoint,
    MSB_EVENT_TYPE.MapOffset: MSBMapOffset,
    MSB_EVENT_TYPE.Navmesh: MSBNavmesh,
    MSB_EVENT_TYPE.Environment: MSBEnvironment,
    MSB_EVENT_TYPE.NPCInvasion: MSBNPCInvasion,
}
