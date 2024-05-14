import numpy as np
ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])
print('initial_array : ', str(ini_array))
result = np.hstack((ini_array, np.atleast_2d(column_to_be_added).T))
print('resultant array', str(result))