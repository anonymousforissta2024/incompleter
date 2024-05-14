test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
print('The original list 1 is : ' + str(test_list1))
print('The original list 2 is : ' + str(test_list2))
res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
print('List after intersection : ' + str(res))