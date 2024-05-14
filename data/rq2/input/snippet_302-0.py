import random

def randomly_interleave(nums1, nums2):
    result = [x.pop(0) for x in random.sample([nums1] * len(nums1) + [nums2] * len(nums2), len(nums1) + len(nums2))]
    return result
nums1 = [1, 2, 7, 8, 3, 7]
print('Original lists:')
print(nums1)
print(nums2)
print('\nInterleave two given list into another list randomly:')
print(randomly_interleave(nums1, nums2))