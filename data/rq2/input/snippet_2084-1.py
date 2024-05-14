test_list = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]
print('The original list : ' + str(test_list))
res = [ele for ele in test_list if len(ele) != K]
print('Filtered list : ' + str(res))