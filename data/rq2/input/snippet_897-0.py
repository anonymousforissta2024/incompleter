import numpy as np
print('Original array:')
print(nums)
print('\nSort the said array by row in ascending order:')
print(np.sort(nums))
print('\nSort the said array by column in ascending order:')
print(np.sort(nums, axis=0))