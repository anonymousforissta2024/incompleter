import numpy as np
print('Original Numpy array:')
print(np_array)
print('Type: ', type(np_array))
print('Sequence: 1,2')
result = repr(np_array).count('1, 2')
print('Number of occurrences of the said sequence:', result)