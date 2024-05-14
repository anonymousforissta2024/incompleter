def addition_subtrction(x, y):
    return (x + y, x - y)
nums2 = [0, 1, 7, 7]
print('Original lists:')
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print('\nResult:')
print(list(result))