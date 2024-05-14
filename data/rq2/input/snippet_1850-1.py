import numpy as np
ini_array2 = np.array([0, 2, 3])
print('initial array', str(ini_array1))
result = ini_array1 * ini_array2[:, np.newaxis]
print('New resulting array: ', result)