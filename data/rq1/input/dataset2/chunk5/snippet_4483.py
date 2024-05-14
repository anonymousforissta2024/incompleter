#Source: https://stackoverflow.com/questions/55288202/adding-uuid-type-to-cerberus-leads-to-bad-type-error
import cerberus

class UUID:
    name = "UUID"

    def __init__(self, potential_uuid: str):
        self.uuid = uuid.UUID(potential_uuid)

    def __str__(self):
        return str(self.uuid)

class Validator(cerberus.Validator):
    def _register_types(self) -> cerberus.Validator.types_mapping:
        types_mapping = Validator.types_mapping.copy()
        for schema_type in datatypes.ALL_TYPES:
            cerberus_type = cerberus.TypeDefinition(
                schema_type.name,
                (schema_type,),
                ())
            types_mapping[schema_type.name] = cerberus_type
        return types_mapping

    cerberus_type = cerberus.TypeDefinition(
        "UUID",
        (datatypes.UUID,),
        ())
    types_mapping = cerberus.Validator.types_mapping.copy()
    types_mapping["UUID"] = cerberus_type

    #def __init__(self, *args, **kwargs ):
    #    types_mapping = self._register_types()
    #    super().__init__(*args, **kwargs)