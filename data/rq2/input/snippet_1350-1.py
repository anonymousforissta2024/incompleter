from operator import eq

def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
print('Original lists:')
print(nums1)
print(nums2)
print('\nNumber of same pair of the said two given lists:')
print(count_same_pair(nums1, nums2))