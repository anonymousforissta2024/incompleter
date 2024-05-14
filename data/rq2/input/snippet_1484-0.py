import json

def encode_complex(object):
    if isinstance(object, complex):
        return [object.real, object.imag]
    raise TypeError(repr(object) + ' is not JSON serialized')
print(complex_obj)