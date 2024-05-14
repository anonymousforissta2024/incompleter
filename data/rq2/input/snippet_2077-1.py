def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res
print('The original list is : ' + str(test_list))
res = []
for i in test_list:
    if i not in res:
        res.append(i)
res = prod(res)
print('Duplication removal list product : ' + str(res))