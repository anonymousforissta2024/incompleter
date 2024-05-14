import numpy as np
print('Original array:\n')
print(nums)
print('\nSort the said array by the nth column: ')
print(nums[nums[:, 1].argsort()])