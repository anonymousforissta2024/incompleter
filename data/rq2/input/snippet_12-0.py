import numpy as np
nums = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print('Original array:')
print(nums)
new_nums = np.zeros(len(nums) + (len(nums) - 1) * p)
new_nums[::p + 1] = nums
print('\nNew array:')
print(new_nums)