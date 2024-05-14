print('The original list is : ' + str(test_list))
K = ' '
res = []
for ele in test_list:
    sub = ele.split(K)
    res.extend(sub)
print('The extended list after split strings : ' + str(res))