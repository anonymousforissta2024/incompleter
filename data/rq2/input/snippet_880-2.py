import numpy as np
x = np.array([200, 300, np.nan, np.nan, np.nan, 700])
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