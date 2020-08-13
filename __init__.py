import bpy
import os
from enum import Enum

bl_info = {
    "name": "Batch Export FBX",
    "category": "Import-Export",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "location": "Info > File > Export > Batch Export",
    "author": "Twiggeh"
}


def register():
    bpy.utils.register_class(BatchExport)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_class(BatchExport)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)


def menu_func(self, context):
    self.layout.operator(BatchExport.bl_idname)


class BatchExport(bpy.types.Operator):
    bl_idname = "file.batch_export"
    bl_label = "Batch Export"
    bl_options = {'REGISTER'}

    filepath = bpy.props.StringProperty(
        name="File Path",
        maxlen=1024,
        subtype="DIR_PATH",
    )

    def execute(self, context):
        bpy.ops.export_scene.fbx(filepath=os.path.join(self.filepath, "each_Collection.fbx"), use_mesh_modifiers=True, mesh_smooth_type='FACE',
                                 batch_mode='COLLECTION', axis_forward='X', axis_up='Y', object_types={"MESH"}, global_scale=.5,
                                 apply_scale_options='FBX_SCALE_ALL', use_subsurf=True, path_mode='COPY', embed_textures=True)

        return {'FINISHED'}

    def invoke(self, context, event):
        self.filepath = ""
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


if __name__ == "__main__":
    register()
