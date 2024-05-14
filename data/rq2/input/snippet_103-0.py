import numpy as np
print('Original array:')
print(nums)
print('\nSorted first 5 elements:')
print(nums[np.argpartition(nums, range(5))])