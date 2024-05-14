import numpy as np
num = np.arange(36)
print('Original array:')
print(arr1)
result = np.where(np.any(arr1 > 10, axis=1))
print('\nRow numbers where at least one item is larger than 10:')
print(result)