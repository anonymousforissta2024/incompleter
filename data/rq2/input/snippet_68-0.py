import numpy as np
print('Original array:')
print(nums)
print('\nTest whether the said array has null columns or not:')
print((~nums.any(axis=0)).any())