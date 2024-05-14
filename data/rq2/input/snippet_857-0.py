import numpy as np
array_nums1 = np.arange(20).reshape(4, 5)
print('Original arrays:')
print(array_nums1)
print(array_nums2)
print('\nAll the nan of array_nums2 replaced by the mean of array_nums1:')
array_nums2[np.isnan(array_nums2)] = np.nanmean(array_nums1)
print(array_nums2)