def is_sort_list(nums):
    result = all((nums[i] <= nums[i + 1] for i in range(len(nums) - 1)))
    return result
nums1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print('Original list:')
print(nums1)
print('\nIs the said list is sorted!')
print(is_sort_list(nums1))
print('\nOriginal list:')
print(nums1)
print('\nIs the said list is sorted!')
print(is_sort_list(nums2))