import random

def randomly_interleave(nums1, nums2):
    result = list(map(next, random.sample([iter(nums1)] * len(nums1) + [iter(nums2)] * len(nums2), len(nums1) + len(nums2))))
    return result
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]
print('Original lists:')
print(nums1)
print(nums2)
print('\nInterleave two given list into another list randomly:')
print(randomly_interleave(nums1, nums2))