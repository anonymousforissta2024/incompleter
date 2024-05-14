#Source: https://stackoverflow.com/questions/62034809/python3-7-metaclassing-from-tuple-base-class-receiving-type-error
from typing import Tuple

class StructMeta(Tuple):
    pass

class Struct(metaclass=StructMeta):
    pass

print(type(Struct))