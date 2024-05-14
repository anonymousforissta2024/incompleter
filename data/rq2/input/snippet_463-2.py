nums2 = [4, 5, 6]
print('Original list:')
print(nums1)
print(nums2)
result = map(lambda x, y: x + y, nums1, nums2)
print('\nResult: after adding two list')
print(list(result))