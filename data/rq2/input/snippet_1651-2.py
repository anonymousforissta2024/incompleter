test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
print('The original list 1 is : ' + str(test_list1))
print('The original list 2 is : ' + str(test_list2))
res = [test_list1[idx] for idx in test_list2]
print('The lists after index elements replacements is : ' + str(res))