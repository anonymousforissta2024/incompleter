import numpy as np
print('Original array:')
print(arr1)
temp = np.ma.masked_array(arr1, np.isnan(arr1))
result = np.mean(temp, axis=1)
print('Averages without NaNs along the said array:')
print(result.filled(np.nan))