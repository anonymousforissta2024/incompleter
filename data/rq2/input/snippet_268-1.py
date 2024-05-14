def is_sort_list(nums):
    result = all((nums[i] <= nums[i + 1] for i in range(len(nums) - 1)))
    return result
print('Original list:')
print(nums1)
print('\nIs the said list is sorted!')
print(is_sort_list(nums1))
nums2 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print('\nOriginal list:')
print(nums1)
print('\nIs the said list is sorted!')
print(is_sort_list(nums2))