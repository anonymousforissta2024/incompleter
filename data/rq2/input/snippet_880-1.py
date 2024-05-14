import numpy as np
y = np.array([[1, 2, 3], [np.nan, 0, np.nan], [6, 7, np.nan]])
print('Original array:')
print(x)
print('After removing nan values:')
result = x[np.logical_not(np.isnan(x))]
print(result)
print('\nOriginal array:')
print(y)
print('After removing nan values:')
result = y[np.logical_not(np.isnan(y))]
print(result)