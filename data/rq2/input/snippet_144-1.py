import functools

def remove_duplicates(nums):
    result = functools.reduce(lambda x, y: x * y, nums, 1)
    return result
nums2 = [2.2, 4.12, 6.6, 8.1, 8.3]
print('list1:', nums1)
print('Product of the said list numbers:')
print(remove_duplicates(nums1))
print('\nlist2:', nums2)
print('Product of the said list numbers:')
print(remove_duplicates(nums2))