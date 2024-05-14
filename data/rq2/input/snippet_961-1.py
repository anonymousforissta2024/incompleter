def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True
nums1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
print('Original list:')
print(nums1)
print('\nIs the said list contains all unique elements!')
print(all_unique(nums1))
print('\nOriginal list:')
print(nums2)
print('\nIs the said list contains all unique elements!')
print(all_unique(nums2))