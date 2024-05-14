def count_same_pair(nums1, nums2, nums3):
    result = sum((m == n == o for m, n, o in zip(nums1, nums2, nums3)))
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums3 = [2, 1, 3, 1, 2, 6, 7, 9]
print('Original lists:')
print(nums1)
print(nums2)
print(nums3)
print('\nNumber of same pair of the said three given lists:')
print(count_same_pair(nums1, nums2, nums3))