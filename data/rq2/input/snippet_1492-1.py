def elementswise_right_join(l1, l2):
    f_len = len(l1) - (len(l2) - 1)
    for i in range(len(l1), 0, -1):
        if i - f_len < 0:
            break
        else:
            l1[i - 1] = l1[i - 1] + l2[i - f_len]
    return l1
nums1 = [2, 4, 7, 0, 5, 8]
print('\nOriginal lists:')
print(nums1)
print(nums2)
print('\nAdd said two lists from left:')
print(elementswise_right_join(nums1, nums2))
nums3 = [1, 2, 3, 4, 5, 6]
nums4 = [2, 4, -3]
print('\nOriginal lists:')
print(nums3)
print(nums4)
print('\nAdd said two lists from left:')
print(elementswise_right_join(nums3, nums4))