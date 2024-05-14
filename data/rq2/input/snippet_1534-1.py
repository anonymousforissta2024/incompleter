test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
print('The original list is : ' + str(test_list))
for sub in test_list:
    res.append([[ele, sub[-1]] for ele in sub[:-1]])
print('The list after pairing is : ' + str(res))