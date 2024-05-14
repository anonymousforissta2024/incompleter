#Source: https://stackoverflow.com/questions/71358734/attributeerror-module-dataclasses-has-no-attribute-is-dataclass
from pydantic import BaseModel, create_model
MyModel = create_model('MyModel', foo="foo")