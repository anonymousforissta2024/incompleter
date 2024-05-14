import numpy as np
print('Original array:')
print(nums)
print('\nNew array after swapping first and last columns of the said array:')
new_nums = nums[:, ::-1]
print(new_nums)