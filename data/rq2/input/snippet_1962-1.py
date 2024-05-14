print('The original list is : ' + str(test_list))
check_matr = [[2, 3], [1, 2], [9, 0]]
res = [ele for ele in check_matr if any((all((a in sub for a in ele)) for sub in test_list))]
print('Matrix row subsets : ' + str(res))