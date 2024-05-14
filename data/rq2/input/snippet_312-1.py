import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print('Array1: ', array1)
print('Array2: ', array2)
print('Unique sorted array of values that are in either of the two input arrays:')
print(np.union1d(array1, array2))