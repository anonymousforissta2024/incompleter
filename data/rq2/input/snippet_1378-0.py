import numpy as np
arr1 = np.reshape(num, [4, 9])
print('Original array:')
print(arr1)
result = np.where(np.any(arr1 > 10, axis=1))
print('\nRow numbers where at least one item is larger than 10:')
print(result)