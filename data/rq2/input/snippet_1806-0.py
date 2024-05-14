test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
print('The original list 1 : ' + str(test_list1))
print('The original list 2 : ' + str(test_list2))
res = [(sub1[1], sub2[1]) for sub2 in test_list2 for sub1 in test_list1 if sub1[0] == sub2[0]]
print('The mapped tuples : ' + str(res))