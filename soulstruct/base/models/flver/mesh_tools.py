"""Tools for manipulating FLVER models, e.g. for Blender import/export."""
from __future__ import annotations

__all__ = [
    "MergedMesh",
    "SplitSubmeshDef",
]

import logging
import typing as tp
from dataclasses import dataclass, field

import numpy as np

from .core import FLVER
from .material import Material
from .submesh import Submesh, FaceSet
from .vertex_array import *

_LOGGER = logging.getLogger("soulstruct")


class SplitSubmeshDef(tp.NamedTuple):
    material: Material
    layout: VertexArrayLayout
    kwargs: dict[str, tp.Any]
    uv_layer_names: list[str] | None = None

    def get_validated_uv_layer_names(self, global_uv_layer_names: tp.Iterable[str], index: int) -> list[str]:
        uv_count = self.layout.get_uv_count()
        uv_layer_names = self.uv_layer_names
        if not uv_layer_names:
            # Default to 'UVMap{i}' for each UV layer.
            uv_layer_names = [f"UVMap{i}" for i in range(uv_count)]
        if len(self.uv_layer_names) != uv_count:
            raise ValueError(
                f"UV layer names for split submesh {index} do not match layout UV count: "
                f"{self.uv_layer_names} does not have {uv_count} elements."
            )
        if any(layer_name not in global_uv_layer_names for layer_name in uv_layer_names):
            raise ValueError(
                f"Not all UV layer names given for split submesh {index} ({uv_layer_names}) appear in the `MergedMesh` "
                f"global UV layer keys ({list(global_uv_layer_names)})."
            )
        return uv_layer_names


@dataclass(slots=True)
class MergedMesh:
    """Holds data for a single merged FLVER mesh created from all its submeshes. Optimized for Blender meshes.

    The merging operation identifes all unique vertices across all submeshes - as defined by their position, bone
    weights, and bone indices - and creates reduced 'vertex arrays' of these data for the entire mesh. Other data
    defined by FLVER vertices are moved to 'loop arrays', as well as the indices of the new reduced vertices they use.
    Each face indexes the loops it uses, as well as the material and vertex buffer layout it uses from the FLVER
    (unchanged indices from the submesh).

    NOTE: Bone indices will be remapped to global bone indices from `submesh.bone_indices` if present. The submesh will
    not be modified and `submesh.bone_indices` will not be cleared.

    Also has the options to discard degenerate (line/point) faces and/or duplicate faces (same three vertex indices in
    any order) as they are encountered. Neither is done by default, as it may be faster for your 3D software (e.g.
    Blender) to handle any issues or exceptions caused by such faces as they arise. Both types of problematic faces
    appear frequently in vanilla FLVER files, likely as an artifact of FromSoft's own mesh-splitting algorithm, and are
    almost certainly fine to remove.

    TODO: Currently optimized for DS1, but likely works for other games (if `FLVER` class is supported for them). Also
     only acts on the first vertex array in each submesh, as I haven't encountered any multi-buffer FLVERs yet.
    """
    vertex_data: np.ndarray  # holds `position`, `bone_weights`, and `bone_indices` fields

    loop_vertex_indices: np.ndarray  # 1D array indexing into `vertex_data` (uint32)

    loop_normals: np.ndarray  # three columns for 'x', 'y', and 'z' (float32)
    loop_normals_w: np.ndarray  # one column for 'w' (uint8)
    loop_tangents: list[np.ndarray]  # four columns per array for 'x', 'y', 'z', and `w` (float32)
    loop_bitangents: np.ndarray  # four columns for 'x', 'y', and 'z' (float32)
    loop_vertex_colors: list[np.ndarray]  # four columns per array for 'r', 'g', 'b', and 'a' (float32)
    # Maps UV layer names (which default to just 'UVMap{i}') to UV data arrays. UV layer names per merged mesh material
    # need to be passed in.
    loop_uvs: dict[str, np.ndarray]  # two columns per array for 'u' and 'v' (float32)  # TODO: ignoring `uv_w`

    faces: np.ndarray  # integer array of `[loop0, loop1, loop2, material_index]` rows (uint32)

    # Stored for posterity and convenient access to materials and layouts.
    flver: FLVER | None = None

    # UV layer names used by each material to assign UV data index.
    material_uv_layers: list[list[str]] | list[None] = field(default_factory=list)

    @classmethod
    def from_flver(
        cls,
        flver: FLVER,
        submesh_material_indices: list[int] = None,
        material_uv_layer_names: list[list[str]] = None,
    ):
        """Construct merged mesh data from all `flver` submeshes.

        The merged `faces` array contains a fourth column (`faces[:, 3]`) that records the 'material index' of each
        face, which is sourced directly from argument `submesh_material_indices` (which should have the same length as
        `flver.submeshes`) rather than using the original FLVER material index. This allows the definition of 'material'
        to be set to match the caller's purposes for the merged mesh, usually to preserve distinct submesh or face set
        properties (e.g. `is_bind_pose` or `use_backface_culling`) that may be different for submeshes that share the
        same FLVER material index.

        If `material_uv_layer_names` is given, it should be a list of list of UV layer names that correspond to the UV
        subarrays in the submesh's vertex buffer. This ensures that the UV maps across the entire merged FLVER are as
        compatible as possible, e.g. second textures UVs go into one map, lightmap UVs go into one map, etc. If not
        given, UV data will be assigned to default 'UVMap{i}' names created directly from the vertex array indices,
        which may lead to clashes and a more difficult 3D workflow (though no lost information, theoretically).
        """
        if not flver.submeshes:
            raise ValueError("FLVER has no submeshes. Cannot create `MergedMesh`.")

        if not submesh_material_indices:
            # By default, every submesh will be considered a separate 'material' in the `MergedMesh`.
            submesh_material_indices = list(range(len(flver.submeshes)))

        valid_submeshes = []
        valid_submesh_material_indices = []
        for i, submesh in enumerate(flver.submeshes):
            if any(
                "position" in vertex_array.array.dtype.names
                and np.isnan(vertex_array.array["position"]).any()
                for vertex_array in submesh.vertex_arrays
            ):
                _LOGGER.warning(f"Submesh {i} has NaN vertex position data and will be ignored by `MergedMesh`.")
                continue

            valid_submeshes.append(submesh)
            valid_submesh_material_indices.append(submesh_material_indices[i])

        all_vertices, loop_data_dict = cls.build_stacked_loops(
            valid_submeshes, valid_submesh_material_indices, material_uv_layer_names
        )

        vertex_data, loop_vertex_indices, faces = cls.merge_vertices(
            valid_submeshes,
            all_vertices,
            valid_submesh_material_indices,
            loop_data_dict["loop_normals"],
        )

        return cls(
            vertex_data=vertex_data,
            loop_vertex_indices=loop_vertex_indices,
            **loop_data_dict,
            faces=faces,
            flver=flver,
        )

    @classmethod
    def build_stacked_loops(
        cls,
        submeshes: list[Submesh],
        material_indices: list[int],
        material_uv_layer_names: list[list[str]] | None,
    ) -> tuple[np.ndarray, dict[str, np.ndarray]]:
        """Row-stack all submesh vertices' position and bone data in a single structured array for reduction."""
        # TODO: None of these fields are guaranteed in later games.
        dtype = [
            ("position", "f", 3),  # TODO: support 4D position
            ("bone_weights", "f", 4),
            ("bone_indices", "i", 4),
        ]
        total_vertex_count = sum(len(mesh.vertices) for mesh in submeshes)

        # Structured array for mixed dtypes.
        all_vertices = np.empty(total_vertex_count, dtype=dtype)  # will be fully initialized

        # These four arrays will be fully initialized.
        loop_normals = np.empty((total_vertex_count, 3), dtype=np.float32)
        loop_normals_w = np.empty((total_vertex_count, 1), dtype=np.uint8)  # still 2D!
        loop_bitangents = np.empty((total_vertex_count, 4), dtype=np.float32)

        loop_tangents_dict = {}  # new arrays added as new tangent indices are encountered
        loop_vertex_colors_dict = {}  # new arrays added as new color indices are encountered
        loop_uvs = {}  # type: dict[str, np.ndarray]  # new arrays added as new global UV layer names used

        offset = 0
        for submesh, material_index in zip(submeshes, material_indices):
            vertices = submesh.vertex_arrays[0].array
            field_names = vertices.dtype.names
            i = offset
            offset += len(vertices)
            j = offset

            submesh_vertices = all_vertices[i:j]

            if "position" in field_names:
                submesh_vertices["position"] = vertices["position"]
            else:
                _LOGGER.warning("Submesh vertices have no 'position' data. This is very unusual. Using zeroes.")
                submesh_vertices["position"] = 0.0

            if "bone_weights" in field_names:
                submesh_vertices["bone_weights"] = vertices["bone_weights"]
            else:  # no bone weights (standard in map piece FLVERs)
                submesh_vertices["bone_weights"] = 0.0

            if "bone_indices" in field_names:
                bone_indices = vertices["bone_indices"]
                if submesh.bone_indices is not None:
                    # Remap local to global bone indices (without modifying FLVER).
                    bone_indices = submesh.bone_indices[bone_indices]
                submesh_vertices["bone_indices"] = bone_indices
            else:
                # This is unusual in DS1, but not beyond that.
                submesh_vertices["bone_indices"] = 0

            if "normal" in field_names:
                loop_normals[i:j] = vertices["normal"]
            else:
                # Default to upward (Y) vector.
                loop_normals[i:j] = [0.0, 1.0, 0.0]

            if "normal_w" in field_names:
                loop_normals_w[i:j] = vertices["normal_w"]
            else:
                # Default to 127.
                loop_normals_w[i:j] = 127

            if "bitangent" in field_names:
                loop_bitangents[i:j] = vertices["bitangent"]
            else:
                # Default to forward (Z) vector.
                loop_bitangents[i:j] = [0.0, 0.0, 1.0, 1.0]

            # Tangent, color, and UV arrays are only created as used. They are created with `np.zeros()` so any vertices
            # that don't use a given tangent, color or UV index will be zeroes.
            for name in field_names:
                if name.startswith("tangent_"):
                    # TODO: Might want to default to, say, a rightward unit vector rather than zeroes.
                    t_i = int(name[-1])
                    tangent_array = loop_tangents_dict.setdefault(
                        t_i, np.zeros((total_vertex_count, 4), dtype=np.float32)
                    )
                    tangent_array[i:j] = vertices[f"tangent_{t_i}"]
                elif name.startswith("color_"):
                    c_i = int(name[-1])
                    color_array = loop_vertex_colors_dict.setdefault(
                        c_i, np.zeros((total_vertex_count, 4), dtype=np.float32)
                    )
                    color_array[i:j] = vertices[f"color_{c_i}"]
                elif name.startswith("uv_"):
                    uv_i = int(name.removeprefix("uv_"))
                    uv_layer_name = f"UVMap{uv_i}"  # default
                    if material_uv_layer_names:
                        try:
                            uv_layer_name = material_uv_layer_names[material_index][uv_i]
                        except IndexError:
                            _LOGGER.warning(f"No UV layer name for material index {material_index} (UV {uv_i}).")
                    uv_array = loop_uvs.setdefault(
                        uv_layer_name, np.zeros((total_vertex_count, 2), dtype=np.float32)  # TODO: support `uv[2]`
                    )
                    uv_array[i:j] = vertices[name]

        # Could be empty lists.
        loop_tangents = [loop_tangents_dict[i] for i in sorted(loop_tangents_dict)]
        loop_vertex_colors = [loop_vertex_colors_dict[i] for i in sorted(loop_vertex_colors_dict)]
        # NOTE: We don't sort `loop_uvs`. Their order shouldn't matter; the user can determine it, if needed.

        return all_vertices, dict(
            loop_normals=loop_normals,
            loop_normals_w=loop_normals_w,
            loop_tangents=loop_tangents,
            loop_bitangents=loop_bitangents,
            loop_vertex_colors=loop_vertex_colors,
            loop_uvs=loop_uvs,
        )

    @classmethod
    def merge_vertices(
        cls,
        submeshes: list[Submesh],
        all_vertices: np.ndarray,
        submesh_material_indices: list[int],
        loop_normals: np.ndarray,
    ):
        """
        Problem: blindly merging vertices does NOT always work, because sometimes FLVER models have two faces with
        vertices in identical positions (and with identical bones) but with inverted normals, whether they be in the
        same or different material (not sure yet exactly which case happens).

        Unfortunately, this forces us to iterate over faces, rather than vertices, and manually compare face normals
        (averaged over their loops) with `np.dot` to determine whether they should use the same vertices or not.

        TODO: First pass at this; not necessarily optimal, though I'm short on ideas for improving it.

        Let's imagine a per-face approach:
            - combine all vertices in all submeshes but do NOT reduce them yet
            - instead, keep a dictionary mapping vertex (position, bone_weights, bone_indices) to full vertex row
                - these represent the ordered, 'created' merged vertices
            - also create a 'vertex variant' dictionary mapping the same hashes to inner dicts that map normals to
                vertex rows
            - iterate over faces in submesh
            - for each vertex in face:
                - hash vertex by (position, bone_indices, bone_weights)
                - try to retrieve vertex hash
                    - if missing, add it to the dictionary (first-time Blender vertex) and use its index
                    - if present, compare dot product of normals for each value in the 'vertex variant' subdict:
                        - if dot product is < -0.9, the existing Blender vertex is NOT suitable; normals change too much
                        - create a new 'vertex variant' normal key under this (position, bone_indices, bone_weights) key
                - if ALL THREE vertex hashes are already present, and the normals are all 'mergeable', then:
                    - we need to check a third dictionary that tells us which material index added the duplicate face
                    - if it's different, create new vertices anyway (different materials with identical face positions)
                    - if it's the same, we seem to have a genuine "duplicate" same-material face that should be ignored
            - Blender vertex list and properly indexed face list are now ready!

        Note that the above algorithm does not really care when it encounters packed FLVER faces that seem to use
        vertices with wildly varying normals (e.g. one of the vertex normals is inverted from the other two).
        """

        # Maps vertex raw data to its vertex index and the loop normal of its first face. Two variant dicts; the second
        # is only used if a face has a near-inverted normal from the vertices retrieved from the first variant. (No more
        # than two vertex variants can exist, as no other vertex normal could possibly be different enough from both.)
        vertex_indices_normals = {}  # type: dict[bytes, tuple[int, np.ndarray]]
        inv_vertex_indices = {}  # type: dict[bytes, int]  # normal not stored
        # Actual vertex indices to extract from `all_indices`.
        reduced_vertex_indices = []  # type: list[int]
        vertex_count = 0  # rather than continually check `len(reduced_vertex_indices)`
        # List of final faces: `(loop0, loop1, loop2)`, which naturally excludes duplicates. Material index added later.
        all_submesh_faces = []  # type: list[np.ndarray]

        # Array of loop vertex indices. Same length as other loop data, as face loop indices are not modified (beyond
        # offsetting them for each merged submesh).
        loop_vertex_indices = np.empty(len(loop_normals), dtype=np.uint32)
        assigned_loop_indices = set()

        loop_offset = 0
        for i, (submesh, material_index) in enumerate(zip(submeshes, submesh_material_indices)):

            triangles = submesh.face_sets[0].triangulate(allow_primitive_restarts=False)  # `(n, 3)` array
            triangles += loop_offset

            submesh_faces_list = []  # type: list[np.ndarray]

            for triangle in triangles:
                for loop_index in triangle:

                    if loop_index in assigned_loop_indices:
                        continue

                    assigned_loop_indices.add(loop_index)

                    # TODO: If this `loop_index` has already been checked, we should be able to skip it, as a previous
                    #  face will have already assigned the vertex data index of that loop. The whole point of merging
                    #  is to check whether DIFFERENT native FLVER 'loops' (vertices) can be merged, particularly where
                    #  one material changes to another.

                    triangle_vert = all_vertices[loop_index]
                    vert_normal = loop_normals[loop_index]
                    vertex_hash = triangle_vert.tobytes()

                    # Check for an existing vertex with the same (position, bone_weights, bone_indices) data.
                    try:
                        existing_vertex_index, existing_normal = vertex_indices_normals[vertex_hash]
                    except KeyError:
                        # First time this vertex has been encountered.
                        vertex_index = vertex_count
                        vertex_indices_normals[vertex_hash] = (vertex_index, vert_normal)
                        loop_vertex_indices[loop_index] = vertex_index
                        reduced_vertex_indices.append(loop_index)
                        vertex_count += 1
                        continue

                    # Compare normals to see if this vertex is suitable.
                    if np.dot(vert_normal, existing_normal) < -0.9:
                        # This face is inverted from the existing vertex. Use the inv dict (whether existing or new).
                        try:
                            existing_inv_vertex_index = inv_vertex_indices[vertex_hash]
                        except KeyError:
                            # First time this inverted vertex has been encountered.
                            vertex_index = vertex_count
                            inv_vertex_indices[vertex_hash] = vertex_index
                            reduced_vertex_indices.append(loop_index)
                            loop_vertex_indices[loop_index] = vertex_index
                            vertex_count += 1
                            continue

                        # Use existing inverted vertex. We do NOT check for normals here; if it turns out that another
                        # face has already used the exact same three inverted vertices, it will be treated as a true
                        # 'duplicate face' and handled accordingly (e.g. simply discarded in Blender).
                        loop_vertex_indices[loop_index] = existing_inv_vertex_index
                        continue

                    # Existing vertex is suitable (normal is sufficiently close). Again, if it turns out that multiple
                    # faces use the exact same three vertices, they will be treated as a true 'duplicate face'.
                    # TODO: Duplicate same-side faces should at least be supported across materials?
                    loop_vertex_indices[loop_index] = existing_vertex_index

                submesh_faces_list.append(triangle)

            submesh_faces = np.column_stack(
                [submesh_faces_list, np.full(len(submesh_faces_list), material_index, dtype=np.uint32)]
            )
            all_submesh_faces.append(submesh_faces)

            loop_offset += len(submesh.vertex_arrays[0])

        vertex_data = all_vertices[reduced_vertex_indices]
        faces = np.row_stack(all_submesh_faces)
        loop_vertex_indices = np.array(loop_vertex_indices, dtype=np.uint32)
        return vertex_data, loop_vertex_indices, faces

    @staticmethod
    def is_triangle_degenerate(
        triangle_vertex_indices: tuple[int, int, int],
        discard_degenerate_faces=False,
        discard_duplicate_faces=False,
        existing_face_set: set = None,
    ):
        """Returns True if triangle has two or more identical vertex indices or already exists in some vertex order."""
        if discard_degenerate_faces:
            if len(set(triangle_vertex_indices)) < 3:
                return True  # face with duplicate vertices
        if discard_duplicate_faces:
            if (triangle_tuple := tuple(sorted(triangle_vertex_indices))) in existing_face_set:
                return True  # face with same three vertices in any order
            existing_face_set.add(triangle_tuple)
        return False

    def swap_vertex_yz(self, tangents=True, bitangents=True):
        """Transform mesh in-place from game to Blender coordinates (or back) by swapping Y and Z columns of the
        relevant columns.

        As a minor optimization for Blender import, has the option to ignore tangents or bitangents.
        """
        self.vertex_data["position"] = self.vertex_data["position"][:, [0, 2, 1]]
        self.loop_normals = self.loop_normals[:, [0, 2, 1]]
        if tangents:
            for i, tangent_array in enumerate(self.loop_tangents):
                self.loop_tangents[i] = tangent_array[:, [0, 2, 1, 3]]
        if bitangents:
            self.loop_bitangents = self.loop_bitangents[:, [0, 2, 1, 3]]

    def invert_vertex_uv(self, invert_u=False, invert_v=True):
        """Transform loop UV data in place by subtracting UV coordinates from 1.

        Inverts only V by default, as this is standard for Blender.

        TODO: `uv_w` support.
        """
        for loop_uv_array in self.loop_uvs.values():
            if invert_u:
                loop_uv_array[:, 0] = 1.0 - loop_uv_array[:, 0]
            if invert_v:
                loop_uv_array[:, 1] = 1.0 - loop_uv_array[:, 1]

    def normalize_normals(self):
        """Transform loop normal data in place by normalizing them.

        As normals are typically compressed in FLVER vertex buffers, the decompressed normals are not normalized by
        default. They are not normalized automatically by Soulstruct because this is lossy. However, Blender expects
        normalized vectors for its normal data, so this method is provided to normalize them in-place.
        """
        self.loop_normals /= np.linalg.norm(self.loop_normals, axis=1, keepdims=True)

    def split_mesh(
        self,
        split_submesh_defs: list[SplitSubmeshDef],
        use_submesh_bone_indices=True,
        max_bones_per_submesh=38,
        unused_bone_indices_are_minus_one=False,
    ) -> list[Submesh]:
        """Splits merged mesh into FLVER submeshes.

        `split_submesh_defs` must be a list of FLVER `Material` instances, appropriate layouts, and combined
        `Submesh/FaceSet` kwargs for each value that appears in `faces[:, 3]`. The merged mesh will be split based on
        these values (and maybe further split by bone maximum if `use_submesh_bone_indices == True`) and the created
        `Submesh` and `FaceSet` instances will take their materials, layouts, and miscellaneous kwargs from this list.

        If `uv_layer_names` is given for a `split_submesh_defs` element, it should be a list of list of UV layer
        names that indicate which keys in `MergedMesh.loop_uvs` are used by each corresponding submesh. This will
        ensure that each FLVER submesh vertex buffer can tightly pack only the global arrays that it uses: for
        example, a lightmapped one-texture submesh material may have UV layer names `['UVTexture0', 'UVLightmap']`,
        which will become its `uv_0` and `uv_1` vertex buffer fields, respectively. If `submesh_uv_layer_names` is
        not given, each submesh will simply look up UV keys 'UVMap{i}' in `MergedMesh.loop_uvs` for `i < n`,
        where `n` is the number of UVs it uses (determined by its given layout). This is fine, assuming that the
        `MergedMesh` was also constructed this way, with no UV layer names given.

        As with `MergedMesh.from_flver()`, the definition of 'material' here should comprise any reason that the mesh
        needs to be split, and `faces[3]` should be set accordingly. Two split submeshes may use the same FLVER
        material in `split_submesh_defs`, for example, yet have different `is_bind_pose` values or `face_sets[
        0].use_backface_culling` etc. The `FLVER` class will efficiently remove any duplicate FLVER materials or
        layouts when packed.

        If a submesh material index has no faces, it will be ignored.

        `is_bind_pose` must appear in each submesh kwargs dictionary, as it is used to determine bone index style.
        TODO: Still not 100% sure if there are any FLVERs that use 'bind pose' for some submeshes but not others. From
         memory, I found a few cut content objects or something, but only checked the bool and not the indices.

        If `unused_bone_indices_are_minus_one` is True, it will be assumed that the bone indices in
        `self.vertex_bone_indices` have been set to -1 when unused, rather than the FLVER standard of zero (which can be
        confused with actual use of bone 0 and requires weight inspection to confirm). This makes mesh splitting easier
        when submesh bone indices are used (with maximums); all the -1 indices will be replaced with zeroes in the final
        split submesh arrays.
        """
        if use_submesh_bone_indices and max_bones_per_submesh < 3:
            raise ValueError("`max_bones_per_submesh` must be >= 3 (and realistically should be much higher).")

        # Split each `SplitSubmeshDef` into its component information for efficiency.
        submesh_materials = [submesh_def.material for submesh_def in split_submesh_defs]
        submesh_layouts = [submesh_def.layout for submesh_def in split_submesh_defs]
        submesh_kwargs = [submesh_def.kwargs for submesh_def in split_submesh_defs]
        submesh_uv_layer_names = [
            submesh_def.get_validated_uv_layer_names(self.loop_uvs, i)
            for i, submesh_def in enumerate(split_submesh_defs)
        ]

        # We construct two material dtypes: one that uses global UV layer names, and the true one that uses tightly
        # packed 'uv_{i}' UV names. These names are the only difference, so we can just reassign the dtype at the end.
        global_uv_material_dtypes = []
        true_material_dtypes = []
        for layout, uv_layer_names in zip(submesh_layouts, submesh_uv_layer_names):
            true_dtype = layout.get_dtypes()[1]  # decompressed fields
            global_dtype_fields = []
            for field_name, (field_fmt, field_index) in true_dtype.fields.items():
                if field_name.startswith("uv_"):
                    local_uv_index = int(field_name.removeprefix("uv_"))
                    global_uv_layer_name = uv_layer_names[local_uv_index]
                    global_dtype_fields.append((global_uv_layer_name, field_fmt))
                else:
                    global_dtype_fields.append((field_name, field_fmt))
            global_dtype = np.dtype(global_dtype_fields)
            global_uv_material_dtypes.append(global_dtype)
            true_material_dtypes.append(true_dtype)

        # We construct a `dtype` that includes all fields from every material.
        # Order doesn't matter here, as materials will retrieve the combined columns they need by name, not index.
        combined_dtype_fields = []
        for dtype in global_uv_material_dtypes:
            for field_name, (field_fmt, field_index) in dtype.fields.items():
                if (field_name, field_fmt) not in combined_dtype_fields:
                    combined_dtype_fields.append((field_name, field_fmt))
        combined_dtype = np.dtype(combined_dtype_fields)

        # First, construct a big merged array of all FLVER-style loops (i.e. containing vertex AND loop data per row
        # rather than being true face corners). Vertex data (position and bones) will repeat in every loop that uses it.
        # Note that UV layers still have their global names; final split submeshes will rename them `uv_0`, `uv_1`, etc.
        merged_loops = self.get_combined_loop_data(combined_dtype)

        # Stores tuples of `(material_index, loop_array, submesh_bone_indices)` for each submesh. Every three rows in
        # `loop_array` comprises a unique face, so face indices are implicit.
        # These are further subsplit by bone maximum if applicable. Loop arrays have not yet been reduced down to unique
        # rows only (happens afterward).
        # NOTE: Data will be EXTRACTED from `merged_loops` by index, making no assumptions about which submeshes share
        # loop data (which will never happen when `MergedMesh` is constructed from a single FLVER, but may in custom
        # data).
        split_submesh_info = []  # type: list[tuple[int, np.ndarray, tp.Optional[np.ndarray]]]

        merged_loop_views = {}  # minor optimization (construct each dtype-dependent view only once)
        for material_index, global_uv_material_dtype in enumerate(global_uv_material_dtypes):

            # Split `faces` and indexed `merged_loops` by material index (column 3).
            submesh_faces = self.faces[self.faces[:, 3] == material_index][:, :3]  # `(n, 3)` array
            if len(submesh_faces) == 0:
                # This is an unused material index. Do not create any submeshes.
                continue
            submesh_loop_indices = submesh_faces.ravel()  # all loop indices used by faces in this submesh

            # Loop data access. This makes no assumptions about how 'loopy' the loop data in the `MergedMesh` is. If
            # loaded from a FLVER, many faces will already index the same 'loops', but this may not be the case for
            # custom data (like true loops from a Blender mesh). This array will always have length `(3 * n, 3)`, where
            # `n` is the face count; faces with overlapping loop indices will just have duplicate rows, all of which
            # will be reduced to unique rows below. The face indices at this stage are also implicit: [0, 1, 2, 3, ...]
            dtype_view = merged_loop_views.setdefault(
                global_uv_material_dtype.names, merged_loops[list(global_uv_material_dtype.names)]
            )
            # Every three rows corresponds to a single face (will have many duplicates that are removed below).
            submesh_loops = dtype_view[submesh_loop_indices]

            if use_submesh_bone_indices:
                split_submesh_info += self.subsplit_faces(
                    material_index,
                    submesh_loops,
                    is_bind_pose=submesh_kwargs[material_index]["is_bind_pose"],
                    max_bones_per_submesh=max_bones_per_submesh,
                    unused_bone_indices_are_minus_one=unused_bone_indices_are_minus_one,
                )
            else:
                # Vertex bone indices are global and have no maximum count.
                split_submesh_info.append((material_index, submesh_loops, None))

        split_submeshes = []

        for material_index, submesh_loops, submesh_bone_indices in split_submesh_info:
            kwargs = submesh_kwargs[material_index].copy()  # may be used by multiple subsplit meshes

            # Duplicate loop data is finally removed here, giving the true vertex data stored in the FLVER submesh.
            # However, since `np.unique()` automatically and unstoppably sorts the array, we need to use `return_index`
            # to UNSORT it, then `return_inverse` (after also unsorting) to get the final face vertex indices.
            submesh_vertices, first_indices, face_vertex_indices = np.unique(
                submesh_loops, return_index=True, return_inverse=True, axis=0
            )
            # Get the sorting indices for `first_indices`. The elements in this are the indices of elements that would
            # produce a sorted version of `first_indices`:
            sorting_indices = np.argsort(first_indices)
            # Apply those to `submesh_vertices` (sorted output of `np.unique` above) to unsort it:
            submesh_vertices = submesh_vertices[sorting_indices]
            # Get the inverse sorting indices, i.e. the indices of elements in `first_indices`:
            inverse_sorting_indices = np.argsort(sorting_indices)
            # Apply to `face_indices` to update them to index into the unsorted `submesh_vertices`:
            face_vertex_indices = inverse_sorting_indices[face_vertex_indices]

            if unused_bone_indices_are_minus_one:
                # Replace -1 unused bone indices with 0 for FLVER.
                bone_indices = submesh_vertices["bone_indices"]
                bone_indices[bone_indices == -1] = 0

            # Reassign true dtype to vertex array (with local 'uv_{i}' names instead of merged global UV layer names).
            submesh_vertices = submesh_vertices.astype(true_material_dtypes[material_index], copy=False)

            vertex_array = VertexArray(array=submesh_vertices, layout=submesh_layouts[material_index])

            face_set_count = kwargs.pop("face_set_count", 1)
            face_set = FaceSet.from_triangles(
                face_vertex_indices, use_backface_culling=kwargs.pop("use_backface_culling")
            )
            material = submesh_materials[material_index]
            submesh = Submesh(
                face_sets=[face_set],
                material=material,
                vertex_arrays=[vertex_array],
                bone_indices=submesh_bone_indices,
                **kwargs,  # typically just 'is_bind_pose', 'default_bone_index', and maybe 'uses_bounding_box'
            )
            submesh.refresh_bounding_box()

            if face_set_count > 1:
                # Duplicate default face set (0) to all later ones (same instance!).
                submesh.face_sets += [submesh.face_sets[0] for _ in range(face_set_count - 1)]

            split_submeshes.append(submesh)

        return split_submeshes

    @staticmethod
    def subsplit_faces(
        material_index: int,
        submesh_loops: np.ndarray,
        is_bind_pose: bool,
        max_bones_per_submesh: int,
        unused_bone_indices_are_minus_one: bool,
    ) -> list[tuple[int, np.ndarray, np.ndarray]]:
        """Takes arrays of split faces, loops, and bone indices and returns a tuple of arrays of subsplit faces, loops,
        and bone indices, which can be appended to the appropriate lists for each material rather than a single
        submesh."""
        subsplit_face_indices = [0]
        subsplit_bone_indices = []

        bone_indices = submesh_loops["bone_indices"]  # copied below if modified

        if is_bind_pose:
            # Up to four unique bones per vertex, so we need to more carefully collect as we go.
            if not unused_bone_indices_are_minus_one:
                # Set all unused bone indices to -1, to distinguish them from true use of bone 0. Ideally, the
                # user can do this themselves while they are constructing their merged mesh (e.g. from Blender)
                # to save time here, as this requires two new array creations.
                bone_weights = submesh_loops["bone_weights"]
                bone_indices = bone_indices.copy()  # NOT modified in-place
                bone_indices[bone_weights == 0.0] = -1

        # Loops are still genuine loops, i.e. every three represent one triangle with 12 total bone indices.
        all_face_bone_indices = bone_indices.reshape((-1, 12))

        # Rather than filtering out values of -1, we make sure it's always in the set, and offset the check.
        # Slightly suboptimal for `is_bind_pose = False`, as every face should only have up to 3 bones, but
        # worth the complexity trade-off.
        max_bones = max_bones_per_submesh + 1
        unique_indices = {-1}
        for face_index, face_bone_indices in enumerate(all_face_bone_indices):
            new_indices = unique_indices | set(face_bone_indices)
            if len(new_indices) > max_bones:
                # This row would exceed the limit. Start a new submesh.
                subsplit_face_indices.append(face_index)
                subsplit_bone_indices.append(np.array(sorted(unique_indices - {-1})))
                unique_indices = {-1} | set(face_bone_indices)
            else:
                # Can continue.
                unique_indices = new_indices

        # Finish final subsplit. Face indices for submeshes that don't need sub-splitting will just be `[0, n]`.
        subsplit_face_indices += [len(submesh_loops) // 3]
        subsplit_bone_indices.append(np.array(sorted(unique_indices - {-1})))

        all_subsplits = []
        for i, face_start in enumerate(subsplit_face_indices[:-1]):
            face_end = subsplit_face_indices[i + 1]
            loops_start, loops_end = face_start * 3, face_end * 3
            subsplit_loops = submesh_loops[loops_start:loops_end]

            subsplit_global_bone_indices = bone_indices[loops_start:loops_end, :]
            subsplit_loops["bone_indices"] = MergedMesh.make_bone_indices_local(
                subsplit_global_bone_indices, subsplit_bone_indices[i]
            )

            all_subsplits.append((material_index, subsplit_loops, subsplit_bone_indices[i]))

        return all_subsplits

    def get_combined_loop_data(self, combined_dtype: np.dtype):
        """Combine the appropriate loop data, in the given order, into a single structured array for indexing by loop
        row ('FLVER vertex row') or field name (so submesh materials can retrieve only the fields they need).

        The returned array, therefore, is essentially a merged version of the complete FLVER `submesh.vertices` arrays
        for all submeshes using a 'maximal' dtype.

        The only exception is the UV data arrays, whose fields still have their global names (e.g. 'UVTexture0' or
        'UVMap1'). The final split submeshes will simply rename the fields they actually use and discard the remainder.

        Note that the order of fields in `combined_dtype` likely won't matter if materials are using their own subset
        dtypes anyway.
        """
        loop_count = len(self.loop_vertex_indices)
        combined_array = np.empty(loop_count, dtype=combined_dtype)  # will be fully initialized

        names = set(combined_dtype.names)  # order is unimportant for initialization

        if "position" in names:
            positions = self.vertex_data["position"][self.loop_vertex_indices]  # (loop_count, 3)
            combined_array["position"] = positions
        if "bone_weights" in names:
            bone_weights = self.vertex_data["bone_weights"][self.loop_vertex_indices]  # (loop_count, 4)
            combined_array["bone_weights"] = bone_weights
        if "bone_indices" in names:
            bone_indices = self.vertex_data["bone_indices"][self.loop_vertex_indices]  # (loop_count, 4)
            combined_array["bone_indices"] = bone_indices
        if "normal" in names:
            combined_array["normal"] = self.loop_normals
        if "normal_w" in names:
            combined_array["normal_w"] = self.loop_normals_w
        if "bitangent" in names:
            combined_array["bitangent"] = self.loop_bitangents

        tangent_names = [n for n in names if n.startswith("tangent_")]
        for tangent_name in tangent_names:
            t_i = int(tangent_name[-1])
            combined_array[f"tangent_{t_i}"] = self.loop_tangents[t_i]  # (loop_count, 4)

        # Combined array still uses global UV layer names.
        for uv_layer_name in self.loop_uvs:
            combined_array[uv_layer_name] = self.loop_uvs[uv_layer_name]

        color_names = [n for n in names if n.startswith("color_")]
        for color_name in color_names:
            c_i = int(color_name[-1])
            combined_array[f"color_{c_i}"] = self.loop_vertex_colors[c_i]  # (loop_count, 4)

        return combined_array

    @staticmethod
    def make_bone_indices_local(bone_indices: np.ndarray, submesh_bone_indices: np.ndarray):
        lo = min(bone_indices.min(), submesh_bone_indices.min())
        hi = max(bone_indices.max(), submesh_bone_indices.max())
        lut = np.zeros(hi - lo + 1, dtype=np.int64)
        lut[submesh_bone_indices - lo] = np.arange(len(submesh_bone_indices))
        return lut[bone_indices - lo]

    @staticmethod
    def unique(array: np.ndarray, max_value=None):
        """More efficient `np.unique()` (for reasonable array lengths) that uses masking and does NOT sort."""
        max_value = max_value or np.max(array) + 1
        used = np.zeros(max_value, dtype=np.uint8)
        used[array] = 1
        return np.argwhere(used == 1)[:, 0]


@dataclass(slots=True)
class SplitSubmesh:
    """Holds data for submeshes under construction."""
    submesh: Submesh

    # Each value added to this (dtype-dependent) will be row-stacked, then the results column-stacked.
    vertex_subarrays: dict[str, list[np.ndarray]]

    # Used to offset face vertex indices
    vertex_count: int

    # Triangles for `FaceSet`.
    face_vertex_indices: list[int]

    @classmethod
    def from_props(cls, **submesh_kwargs):
        """Create a `SplitSubmesh` from a `Submesh`'s properties."""
        return cls(
            submesh=Submesh(**submesh_kwargs),
            vertex_subarrays={},
            vertex_count=0,
            face_vertex_indices=[],
        )
