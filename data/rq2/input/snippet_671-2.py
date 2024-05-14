def addition_subtrction(x, y):
    return (x + y, x - y)
nums1 = [6, 5, 3, 9]
print('Original lists:')
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print('\nResult:')
print(list(result))