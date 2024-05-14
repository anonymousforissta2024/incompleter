import numpy as np
arr1 = np.array([[10, 20, 30], [40, 50, np.nan], [np.nan, 6, np.nan], [np.nan, np.nan, np.nan]])
print('Original array:')
print(arr1)
result = np.mean(temp, axis=1)
print('Averages without NaNs along the said array:')
print(result.filled(np.nan))