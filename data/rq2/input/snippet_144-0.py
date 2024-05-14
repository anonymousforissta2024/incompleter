import functools

def remove_duplicates(nums):
    result = functools.reduce(lambda x, y: x * y, nums, 1)
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('list1:', nums1)
print('Product of the said list numbers:')
print(remove_duplicates(nums1))
print('\nlist2:', nums2)
print('Product of the said list numbers:')
print(remove_duplicates(nums2))