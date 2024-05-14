import numpy as np
print('initial_array : ', str(ini_array))
column_to_be_added = np.array([1, 2, 3])
result = np.hstack((ini_array, np.atleast_2d(column_to_be_added).T))
print('resultant array', str(result))