import numpy as np
print('Original array:')
print(nums)
nums[::2, ::2] = 3
nums[1::2, ::2] = 7
print('\nNew array:')
print(nums)