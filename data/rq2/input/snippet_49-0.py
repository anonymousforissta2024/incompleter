def diff_consecutive_nums(nums):
    result = [b - a for a, b in zip(nums[:-1], nums[1:])]
    return result
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
print('Original list:')
print(nums1)
print('Difference between consecutive numbers of the said list:')
print(diff_consecutive_nums(nums1))
print('\nOriginal list:')
print(nums2)
print('Difference between consecutive numbers of the said list:')
print(diff_consecutive_nums(nums2))