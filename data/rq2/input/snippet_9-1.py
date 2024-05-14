import numpy as np
num = np.arange(18)
arr1 = np.reshape(num, [6, 3])
print('Original array:')
print(arr1)
print('\nExtract upper triangular part of the said array:')
print(result)
result = arr1[np.triu_indices(2)]
print('\nExtract upper triangular part of the said array:')
print(result)