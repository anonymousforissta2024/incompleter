import numpy as np
x = np.arange(16).reshape(4, 4)
print('Original arrays:')
print(x)
print('\nArray with size 2x2 from the said array:')
new_array1 = np.resize(x, (2, 2))
print(new_array1)
print('\nArray with size 6x6 from the said array:')
print(new_array2)