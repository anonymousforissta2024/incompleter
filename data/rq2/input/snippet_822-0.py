import numpy as np
arr1 = np.reshape(num, [4, 9])
print('Original array:')
print(arr1)
result = arr1.sum(axis=0)
print('\nSum of all columns:')
print(result)