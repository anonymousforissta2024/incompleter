print('The original list is : ' + str(test_list))
temp = [ele for sub in test_list for ele in sub]
res = list(zip(*temp))
print('The converted tuple list : ' + str(res))