def elements_difference(nums):
    result = [j - i for i, j in zip(nums[:-1], nums[1:])]
    return result
nums2 = [2, 4, 6, 8]
print('Original list:')
print(nums1)
print('\nDfference between elements (n+1th – nth) of the said list :')
print(elements_difference(nums1))
print('\nOriginal list:')
print(nums2)
print('\nDfference between elements (n+1th – nth) of the said list :')
print(elements_difference(nums2))