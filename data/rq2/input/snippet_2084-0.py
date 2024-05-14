print('The original list : ' + str(test_list))
K = 1
res = [ele for ele in test_list if len(ele) != K]
print('Filtered list : ' + str(res))