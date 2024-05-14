import numpy as np
print('\nOriginal arrays:')
y = x * 3
print('Array-1')
print(x)
print('Array-2')
print(y)
new_array = np.vstack((x, y))
print('\nStack arrays in sequence vertically:')
print(new_array)