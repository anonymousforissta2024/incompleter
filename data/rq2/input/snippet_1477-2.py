from itertools import zip_longest

def elementswise_left_join(l1, l2):
    result = [a + b for a, b in zip_longest(l1, l2, fillvalue=0)][::1]
    return result
nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [3, 3, -1, 7]
print('\nOriginal lists:')
print(nums1)
print(nums2)
print('\nAdd said two lists from left:')
print(elementswise_left_join(nums1, nums2))
nums3 = [1, 2, 3, 4, 5, 6]
print('\nOriginal lists:')
print(nums3)
print(nums4)
print('\nAdd said two lists from left:')
print(elementswise_left_join(nums3, nums4))