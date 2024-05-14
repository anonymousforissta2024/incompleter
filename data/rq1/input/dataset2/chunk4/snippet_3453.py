#Source: https://stackoverflow.com/questions/74685354/typeerror-actor-failed-to-convert-parameter-socket-name-when-calling-functio
level_actors = unreal.EditorLevelLibrary.get_all_level_actors()
filtered_list = unreal.EditorFilterLibrary.by_actor_tag(level_actors, Car_tag, filter_type=unreal.EditorScriptingFilterType.INCLUDE)
actor = filtered_list[0]