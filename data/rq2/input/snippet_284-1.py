def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[1:]):
        if key(e) < key(nums[i]):
            return False
    return True
nums1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print('Original list:')
print(nums1)
print('\nIs the said list is sorted!')
print(is_sort_list(nums1))
print('\nOriginal list:')
print(nums1)
print('\nIs the said list is sorted!')
print(is_sort_list(nums2))