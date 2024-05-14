def dividing_two_lists(l1, l2):
    result = [x / y for x, y in zip(l1, l2)]
    return result
nums1 = [7, 2, 3, 4, 9, 2, 3]
print('Original list:')
print(nums1)
print(nums1)
print(dividing_two_lists(nums1, nums2))