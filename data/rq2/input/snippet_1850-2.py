import numpy as np
ini_array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
print('initial array', str(ini_array1))
result = ini_array1 * ini_array2[:, np.newaxis]
print('New resulting array: ', result)