import unreal

# FBX 파일 경로 설정
fbx_file_path = "C:/path/to/your/file.fbx"

# FBX 임포트 옵션 설정
import_options = unreal.FbxImportOptions()
import_options.set_editor_property("import_mesh", True)
import_options.set_editor_property("import_materials", True)
import_options.set_editor_property("import_animations", True)
import_options.set_editor_property("import_skeletal_mesh", True)
import_options.set_editor_property("import_camera", True)
import_options.set_editor_property("import_lights", True)

# FBX 임포트 실행
task = unreal.AssetImportTask()
task.set_editor_property("filename", fbx_file_path)
task.set_editor_property("destination_path", "/Game/ImportedFBX")
task.set_editor_property("options", import_options)

# 임포트 실행
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

# 임포트된 자산 목록 출력
imported_assets = task.get_editor_property("imported_assets")

# 임포트된 자산의 데이터 확인
has_static_mesh = False
has_skeletal_mesh = False
has_camera = False
has_light = False

for asset in imported_assets:
    asset_name = asset.get_name()
    asset_class = asset.get_class().get_name()
    unreal.log(f"Imported Asset: {asset_name} - Class: {asset_class}")

    # 스태틱 메쉬 확인
    if asset_class == "StaticMesh":
        has_static_mesh = True
        materials = asset.get_materials()
        if materials:
            unreal.log(f"  Static Mesh Materials: {materials}")
        else:
            unreal.log("  Static Mesh: No materials found.")

    # 스켈레탈 메쉬 확인
    elif asset_class == "SkeletalMesh":
        has_skeletal_mesh = True
        animations = asset.get_animations()
        if animations:
            unreal.log(f"  Skeletal Mesh Animations: {animations}")
        else:
            unreal.log("  Skeletal Mesh: No animations found.")

    # 카메라 확인
    elif asset_class == "Camera":
        has_camera = True
        if hasattr(asset, "field_of_view"):
            fov = asset.field_of_view
            unreal.log(f"  Camera Field of View: {fov}")
        else:
            unreal.log("  Camera: No field of view property found.")

    # 라이트 확인
    elif asset_class == "Light":
        has_light = True
        if hasattr(asset, "intensity"):
            intensity = asset.intensity
            unreal.log(f"  Light Intensity: {intensity}")
        else:
            unreal.log("  Light: No intensity property found.")

# 최종적으로 확인된 데이터 출력
if not has_static_mesh:
    unreal.log("No Static Mesh imported.")
if not has_skeletal_mesh:
    unreal.log("No Skeletal Mesh imported.")
if not has_camera:
    unreal.log("No Camera imported.")
if not has_light:
    unreal.log("No Light imported.")
