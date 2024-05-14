def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True
print('Original list:')
print(nums1)
print('\nIs the said list contains all unique elements!')
print(all_unique(nums1))
nums2 = [2, 4, 6, 8, 10, 12, 14]
print('\nOriginal list:')
print(nums2)
print('\nIs the said list contains all unique elements!')
print(all_unique(nums2))