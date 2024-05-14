print('The original list is : ' + str(test_list))
res = []
for sub in test_list:
    res.append([[ele, sub[-1]] for ele in sub[:-1]])
print('The list after pairing is : ' + str(res))