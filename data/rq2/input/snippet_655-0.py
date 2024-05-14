def dividing_two_lists(l1, l2):
    result = [x / y for x, y in zip(l1, l2)]
    return result
nums2 = [9, 8, 2, 3, 3, 1, 2]
print('Original list:')
print(nums1)
print(nums1)
print(dividing_two_lists(nums1, nums2))