import numpy as np
print('Original array:')
print(nums)
print('Indices of elements equal to zero of the said array:')
result = np.where(nums == 0)[0]
print(result)