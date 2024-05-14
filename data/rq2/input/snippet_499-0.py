import numpy as np
print('Original array:')
print(arr1)
result = np.mean(arr1.reshape(-1, 3), axis=1)
print('Average of every consecutive triplet of elements of the said array:')
print(result)