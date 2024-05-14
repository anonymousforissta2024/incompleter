from itertools import zip_longest

def elementswise_right_join(l1, l2):
    result = [a + b for a, b in zip_longest(reversed(l1), reversed(l2), fillvalue=0)][::-1]
    return result
nums1 = [2, 4, 7, 0, 5, 8]
print('\nOriginal lists:')
print(nums1)
print(nums2)
print('\nAdd said two lists from right:')
print(elementswise_right_join(nums1, nums2))
nums3 = [1, 2, 3, 4, 5, 6]
nums4 = [2, 4, -3]
print('\nOriginal lists:')
print(nums3)
print(nums4)
print('\nAdd said two lists from right:')
print(elementswise_right_join(nums3, nums4))