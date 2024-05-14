def elementswise_join(l1, l2):
    result = [x + y for x, y in zip(l1, l2)]
    return result
nums2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
print('Original lists:')
print(nums1)
print(nums2)
print('\nJoin the said two lists element wise:')
print(elementswise_join(nums1, nums2))
list1 = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
list2 = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
print('\nOriginal lists:')
print(list1)
print(list2)
print('\nJoin the said two lists element wise:')
print(elementswise_join(list1, list2))