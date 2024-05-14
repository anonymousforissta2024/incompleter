import numpy as np
nums = np.random.randint(0, 4, (6, 3))
print('Original vector:')
print(nums)
result = nums[~new_nums]
print('\nRows with unequal values:')
print(result)