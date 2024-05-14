import json

def is_complex_num(objct):
    if '__complex__' in objct:
        return complex(objct['real'], objct['img'])
    return objct
simple_object = json.loads('{"real": 4, "img": 3}', object_hook=is_complex_num)
print('Complex_object: ', complex_object)
print('Without complex object: ', simple_object)