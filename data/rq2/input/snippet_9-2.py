import numpy as np
num = np.arange(18)
print('Original array:')
print(arr1)
result = arr1[np.triu_indices(3)]
print('\nExtract upper triangular part of the said array:')
print(result)
result = arr1[np.triu_indices(2)]
print('\nExtract upper triangular part of the said array:')
print(result)