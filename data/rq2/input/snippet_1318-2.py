import numpy as np
print('Original array:')
print(nums)
n = 8.32
r = 18.32
print('\nReplace elements of the said array which are equal to ', n, 'with', r)
print(np.where(nums == n, r, nums))
print('\nReplace elements with of the said array which are less than', n, 'with', r)
print(np.where(nums < n, r, nums))
print('\nReplace elements with of the said array which are greater than', n, 'with', r)
print(np.where(nums > n, r, nums))