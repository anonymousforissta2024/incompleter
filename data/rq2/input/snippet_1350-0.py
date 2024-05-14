from operator import eq

def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
print('Original lists:')
print(nums1)
print(nums2)
print('\nNumber of same pair of the said two given lists:')
print(count_same_pair(nums1, nums2))