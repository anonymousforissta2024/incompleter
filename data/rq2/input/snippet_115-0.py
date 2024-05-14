import numpy as np
print('Original array:')
print(array_nums)
print('\nNew array of shape(5, 4):')
new_array = array_nums.reshape(5, 4)
print(new_array)
print('\nRestore the reshaped array into a 1-D array:')
print(new_array.flatten())