def intersection_nested_lists(l1, l2):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
print('\nOriginal lists:')
print(nums1)
print(nums2)
print('\nIntersection of said nested lists:')
print(intersection_nested_lists(nums1, nums2))