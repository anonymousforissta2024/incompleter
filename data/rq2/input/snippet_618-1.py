import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print('Array1: ', array1)
print('Array2: ', array2)
print('Unique values in array1 that are not in array2:')
print(np.setdiff1d(array1, array2))