def average_two_lists(nums1, nums2):
    result = sum(nums1 + nums2) / len(nums1 + nums2)
    return result
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
print('Original list:')
print(nums1)
print(nums2)
print('\nAverage of two lists:')
print(average_two_lists(nums1, nums2))