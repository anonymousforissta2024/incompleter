import numpy as np
from ast import literal_eval
udict = '{"column0":{"a":1,"b":0.0,"c":0.0,"d":2.0},\n   "column1":{"a":3.0,"b":1,"c":0.0,"d":-1.0},\n   "column2":{"a":4,"b":1,"c":5.0,"d":-1.0},\n   "column3":{"a":3.0,"b":-1.0,"c":-1.0,"d":-1.0}\n  }'
t = literal_eval(udict)
print('\nOriginal dictionary:')
print(t)
print('Type: ', type(t))
print('\nndarray:')
print(result_nparra)
print('Type: ', type(result_nparra))