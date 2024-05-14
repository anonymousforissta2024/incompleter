def diff_consecutive_nums(nums):
    result = [b - a for a, b in zip(nums[:-1], nums[1:])]
    return result
print('Original list:')
print(nums1)
print('Difference between consecutive numbers of the said list:')
print(diff_consecutive_nums(nums1))
nums2 = [4, 5, 8, 9, 6, 10]
print('\nOriginal list:')
print(nums2)
print('Difference between consecutive numbers of the said list:')
print(diff_consecutive_nums(nums2))