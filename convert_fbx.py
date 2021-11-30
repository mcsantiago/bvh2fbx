import bpy
import sys

# Get command line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "—"
bvh_in = argv[0]
fbx_out = argv[0] + ".fbx"

# Import the BVH file
# See https://docs.blender.org/api/current/bpy.ops.import_anim.html?highlight=import_anim#module-bpy.ops.import_anim
bpy.ops.import_anim.bvh(filepath=bvh_in, filter_glob="*.bvh", global_scale=0.0001, frame_start=1, target='ARMATURE',
                        use_fps_scale=False, use_cyclic=False, rotate_mode='NATIVE', axis_forward='Z', axis_up='Y')

# Export as FBX
# See https://docs.blender.org/api/current/bpy.ops.export_scene.html
bpy.ops.export_scene.fbx(filepath=fbx_out, axis_forward='Z',
                         axis_up='Y', use_selection=True, apply_scale_options='FBX_SCALE_NONE')
