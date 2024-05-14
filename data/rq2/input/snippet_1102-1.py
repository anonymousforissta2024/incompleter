def intersection_nested_lists(l1, l2):
    result = [[n for n in lst if n in l1] for lst in l2]
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print('\nOriginal lists:')
print(nums1)
print(nums2)
print('\nIntersection of said nested lists:')
print(intersection_nested_lists(nums1, nums2))