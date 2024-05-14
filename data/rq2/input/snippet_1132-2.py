import numpy as np
from ast import literal_eval
t = literal_eval(udict)
print('\nOriginal dictionary:')
print(t)
print('Type: ', type(t))
result_nparra = np.array([[v[j] for j in ['a', 'b', 'c', 'd']] for k, v in t.items()])
print('\nndarray:')
print(result_nparra)
print('Type: ', type(result_nparra))