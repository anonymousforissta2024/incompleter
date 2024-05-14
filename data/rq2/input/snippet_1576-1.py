import numpy as np
print('Original array:')
print(n_array)
print('\nIndices of elements equal to zero of the given 1-D array:')
res = np.where(n_array == 0)[0]
print(res)