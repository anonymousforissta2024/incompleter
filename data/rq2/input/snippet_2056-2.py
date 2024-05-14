test_list = [('GFg', 5, 9), ('is', 4, 3), ('best', 10, 29)]
print('The original list is : ' + str(test_list))
K = 1
res = [sub for sub in test_list if sub[K] in check_list]
print('The filtered tuples : ' + str(res))