import numpy as np
nums1 = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
nums2 = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
print('Array1:')
print(nums1)
print('\nArray2:')
print(nums2)
nums1 = np.expand_dims(nums1, axis=0)
nums2 = np.expand_dims(nums2, axis=0)
print('\nCombined array:')
print(nums)