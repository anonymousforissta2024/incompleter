import numpy as np
ini_array = np.array([[1.3, 2.5, 3.6, np.nan], [2.6, 3.3, np.nan, 5.5], [2.1, 3.2, 5.4, 6.5]])
print('initial array', ini_array)
col_mean = np.nanmean(ini_array, axis=0)
print('columns mean', str(col_mean))
ini_array[inds] = np.take(col_mean, inds[1])
print('final array', ini_array)