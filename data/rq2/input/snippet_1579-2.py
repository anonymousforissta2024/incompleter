test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]
print('The original list 1 is : ' + str(test_list1))
print('The original list 2 is : ' + str(test_list2))
res = [ele1 for ele1 in test_list1 for ele2 in test_list2 if ele1 == ele2]
print('The Intersection of data records is : ' + str(res))