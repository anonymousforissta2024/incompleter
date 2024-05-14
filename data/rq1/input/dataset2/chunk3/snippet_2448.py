#Source: https://stackoverflow.com/questions/49547647/attributeerror-nonetype-object-has-no-attribute-get-on-rasa-com-and-tensorf
slot_class = Slot.resolve_by_type(slot_dict[slot_name].get("type"))