import numpy as np
print('initial array', ini_array)
col_mean = np.nanmean(ini_array, axis=0)
print('columns mean', str(col_mean))
inds = np.where(np.isnan(ini_array))
ini_array[inds] = np.take(col_mean, inds[1])
print('final array', ini_array)