print('The original list : ' + str(test_list))
K = 2
res = []
for i in test_list:
    freq = test_list.count(i)
    if freq > K and i not in res:
        res.append(i)
print('The required elements : ' + str(res))