import numpy as np
print('Original arrays:')
print(array1)
k = 4
result = np.argpartition(array1, k)
print('\nk smallest values:')
print(array1[result[:k]])