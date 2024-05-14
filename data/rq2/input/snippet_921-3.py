import numpy as np
x = [1, 2, 3]
z = [6, 7]
print('Original arrays:')
print('Array-1')
print(x)
print('Array-2')
print(y)
print('Array-3')
print(z)
new_array = np.array(np.meshgrid(x, y, z)).T.reshape(-1, 3)
print('Combine array:')
print(new_array)