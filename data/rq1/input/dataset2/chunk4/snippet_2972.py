#Source: https://stackoverflow.com/questions/74685354/typeerror-actor-failed-to-convert-parameter-socket-name-when-calling-functio
pos = unreal.Vector(0,0,0)
rot = unreal.Rotator(0,0,0)
ac = unreal.EditorAssetLibrary.load_blueprint_class('/Game/Resim/Blueprints/BP_Camera.BP_Camera')
ac_pos = unreal.EditorLevelLibrary.spawn_actor_from_object(ac, cam_location)