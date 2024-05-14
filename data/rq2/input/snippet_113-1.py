import numpy as np
nums1 = np.ones((2, 2, 3))
print('Original array:')
print(nums1)
new_array = nums1 * nums2[:, :, None]
print('\nNew array:')
print(new_array)