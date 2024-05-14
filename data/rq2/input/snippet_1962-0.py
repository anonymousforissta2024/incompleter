test_list = [[4, 5, 7], [2, 3, 4], [9, 8, 0]]
print('The original list is : ' + str(test_list))
res = [ele for ele in check_matr if any((all((a in sub for a in ele)) for sub in test_list))]
print('Matrix row subsets : ' + str(res))