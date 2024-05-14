import numpy as np
nums1 = np.array([[2, 5, 2], [1, 5, 5]])
print('Array1:')
print(nums1)
print('Array2:')
print(nums2)
print('\nArithmetic means of corresponding elements of said two arrays:')
print(np.divide(np.add(nums1, nums2), 2))