import numpy as np
array1 = np.array([1, 7, 8, 2, 0.1, 3, 15, 2.5])
print('Original arrays:')
print(array1)
result = np.argpartition(array1, k)
print('\nk smallest values:')
print(array1[result[:k]])