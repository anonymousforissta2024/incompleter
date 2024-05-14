def extract_index_ele(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if m == n == o:
            result.append(m)
    return result
nums1 = [1, 1, 3, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 5, 7]
print('Original lists:')
print(nums1)
print(nums2)
print(nums3)
print('\nCommon index elements of the said lists:')
print(extract_index_ele(nums1, nums2, nums3))