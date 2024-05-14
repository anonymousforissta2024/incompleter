from itertools import chain, zip_longest

def interleave_diff_len_lists(list1, list2, list3, list4):
    return [x for x in chain(*zip_longest(list1, list2, list3, list4)) if x is not None]
nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [2, 5, 8]
nums3 = [0, 1]
print('\nOriginal lists:')
print(nums1)
print(nums2)
print(nums3)
print(nums4)
print('\nInterleave said lists of different lengths:')
print(interleave_diff_len_lists(nums1, nums2, nums3, nums4))