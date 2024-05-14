test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
print('The original list : ' + str(test_list))
res = [tuple((j + add_ele for j in sub)) for sub in test_list]
print('List after bulk update : ' + str(res))