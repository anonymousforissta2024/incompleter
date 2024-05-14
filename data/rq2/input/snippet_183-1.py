import numpy as np
print('\nOriginal arrays:')
y = x * 3
print('Array-1')
print(x)
print('Array-2')
print(y)
new_array = np.hstack((x, y))
print('\nStack arrays in sequence horizontally:')
print(new_array)