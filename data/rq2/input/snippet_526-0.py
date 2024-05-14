import numpy as np
print('Original array:')
print(nums)
print('\nDelete the first column of the said array:')
print(np.delete(nums, [0], axis=1))
print('\nDelete the last column of the said array:')
print(np.delete(nums, [4], axis=1))