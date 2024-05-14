import numpy as np
nums2 = np.random.randint(0, 6, (2, 3))
print('Original arrays:')
print(nums1)
print('\n', nums2)
temp = nums1[..., np.newaxis, np.newaxis] == nums2
rows = (temp.sum(axis=(1, 2, 3)) >= nums2.shape[1]).nonzero()[0]
print('\nRows of a given array that contain elements of each row of another given array:')
print(rows)