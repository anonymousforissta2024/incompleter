import numpy as np
print('Original Numpy array:')
print(np_array)
print('Type: ', type(np_array))
result = np.diagonal(np_array, axis1=1, axis2=2)
print('\n2D diagonals: ')
print(result)
print('Type: ', type(result))