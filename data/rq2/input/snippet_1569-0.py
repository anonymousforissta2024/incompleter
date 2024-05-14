print('The original list : ' + str(test_list))
add_ele = 4
res = [tuple((j + add_ele for j in sub)) for sub in test_list]
print('List after bulk update : ' + str(res))