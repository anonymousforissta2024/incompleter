import numpy as np
print('Array1: ', array1)
array2 = [10, 30, 40, 50, 70]
print('Array2: ', array2)
print('Unique values in array1 that are not in array2:')
print(np.setdiff1d(array1, array2))