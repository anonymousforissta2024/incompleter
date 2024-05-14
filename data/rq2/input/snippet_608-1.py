def interleave_diff_len_lists(list1, list2, list3, list4):
    result = []
    l1 = len(list1)
    l2 = len(list2)
    l3 = len(list3)
    l4 = len(list4)
    for i in range(max(l1, l2, l3, l4)):
        if i < l1:
            result.append(list1[i])
        if i < l2:
            result.append(list2[i])
        if i < l3:
            result.append(list3[i])
        if i < l4:
            result.append(list4[i])
    return result
nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [2, 5, 8]
nums4 = [3, 3, -1, 7]
print('\nOriginal lists:')
print(nums1)
print(nums2)
print(nums3)
print(nums4)
print('\nInterleave said lists of different lengths:')
print(interleave_diff_len_lists(nums1, nums2, nums3, nums4))