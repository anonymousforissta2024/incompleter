#Source: https://stackoverflow.com/questions/60740315/typeerror-deserialize-got-an-unexpected-keyword-argument-partial-in-marshm
from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage

from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage


class FileStorageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a valid image."
    }

    def _deserialize(self, value, attr, data) -> FileStorage:
        if value is None:
            return None

        if not isinstance(value, FileStorage):
            self.fail("invalid")

        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)