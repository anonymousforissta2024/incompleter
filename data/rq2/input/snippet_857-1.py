import numpy as np
array_nums2 = np.array([[1, 2, np.nan], [4, 5, 6], [np.nan, 7, np.nan]])
print('Original arrays:')
print(array_nums1)
print(array_nums2)
print('\nAll the nan of array_nums2 replaced by the mean of array_nums1:')
array_nums2[np.isnan(array_nums2)] = np.nanmean(array_nums1)
print(array_nums2)