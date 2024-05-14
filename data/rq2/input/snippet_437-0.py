import numpy as np
arr1 = np.reshape(num, [4, 5])
print('Original array:')
print(arr1)
print([0, 1, 2, 3, 4] in arr1.tolist())
print([0, 1, 2, 3, 5] in arr1.tolist())
print([15, 16, 17, 18, 19] in arr1.tolist())