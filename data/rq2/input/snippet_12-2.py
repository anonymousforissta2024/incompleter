import numpy as np
print('Original array:')
print(nums)
p = 2
new_nums = np.zeros(len(nums) + (len(nums) - 1) * p)
new_nums[::p + 1] = nums
print('\nNew array:')
print(new_nums)