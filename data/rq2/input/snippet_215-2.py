import numpy as np
print('Original vector:')
print(nums)
new_nums = np.logical_and.reduce(nums[:, 1:] == nums[:, :-1], axis=1)
result = nums[~new_nums]
print('\nRows with unequal values:')
print(result)