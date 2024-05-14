import numpy as np
nums = np.random.randint(0, 4, (6, 3))
print('Original vector:')
print(nums)
new_nums = np.logical_and.reduce(nums[:, 1:] == nums[:, :-1], axis=1)
print('\nRows with unequal values:')
print(result)