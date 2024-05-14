import numpy as np
print('Original arrays:')
print(x)
print('\nArray with size 2x2 from the said array:')
new_array1 = np.resize(x, (2, 2))
print(new_array1)
print('\nArray with size 6x6 from the said array:')
new_array2 = np.resize(x, (6, 6))
print(new_array2)