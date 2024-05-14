test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
print('The original list is : ' + str(test_list))
res = [[sub + (cus_eles[idx],) for sub in val] for idx, val in enumerate(test_list)]
print('The matrix after row elements addition : ' + str(res))