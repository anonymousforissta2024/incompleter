#Source: https://stackoverflow.com/questions/55288202/adding-uuid-type-to-cerberus-leads-to-bad-type-error
import cerberus
import uuid


class Validator(cerberus.Validator):
    types_mapping = {
        **cerberus.Validator.types_mapping,
        'UUID': cerberus.TypeDefinition('UUID', (uuid.UUID,), ())
    }