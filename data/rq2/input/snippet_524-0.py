import numpy as np
print('Original array:')
print(my_array)
my_array[:, [0, 1]] = my_array[:, [1, 0]]
print('\nAfter swapping arrays:')
print(my_array)