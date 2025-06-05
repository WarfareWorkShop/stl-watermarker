bl_info = {
    "name": "STL Watermarker",
    "author": "WarfareWorkshop",
    "version": (0, 1),
    "blender": (2, 90, 0),
    "description": "Insert watermark (text) into STL models for identification and traceability",
    "category": "Object",
}

import bpy

def add_watermark_text(obj, text, location=(0, 0, 0)):
    # Create text object
    bpy.ops.object.text_add(location=location)
    text_obj = bpy.context.active_object
    text_obj.data.body = text
    
    # Convert text to mesh
    bpy.ops.object.convert(target='MESH')
    
    # Combine watermark with target object
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    text_obj.select_set(True)
    bpy.ops.object.join()
    
    # Optional: hide the text to keep it invisible in renders
    obj.hide_render = True
    
    return obj

class OBJECT_OT_add_watermark(bpy.types.Operator):
    bl_idname = "object.add_watermark"
    bl_label = "Add Watermark"
    bl_options = {'REGISTER', 'UNDO'}
    
    text: bpy.props.StringProperty(name="Watermark Text", default="WW12345")
    
    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'WARNING'}, "No active object selected")
            return {'CANCELLED'}
        
        add_watermark_text(obj, self.text, location=(0, 0, 0))
        self.report({'INFO'}, f"Watermark '{self.text}' added.")
        return {'FINISHED'}

class OBJECT_PT_watermarker_panel(bpy.types.Panel):
    bl_label = "STL Watermarker"
    bl_idname = "OBJECT_PT_watermarker_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Watermark'
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Insert Watermark into Selected Model")
        layout.operator("object.add_watermark")

def register():
    bpy.utils.register_class(OBJECT_OT_add_watermark)
    bpy.utils.register_class(OBJECT_PT_watermarker_panel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_watermark)
    bpy.utils.unregister_class(OBJECT_PT_watermarker_panel)

if __name__ == "__main__":
    register()
