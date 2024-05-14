test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]
print('The original list 1 : ' + str(test_list1))
print('The original list 2 : ' + str(test_list2))
res = [(sub1[1], sub2[1]) for sub2 in test_list2 for sub1 in test_list1 if sub1[0] == sub2[0]]
print('The mapped tuples : ' + str(res))