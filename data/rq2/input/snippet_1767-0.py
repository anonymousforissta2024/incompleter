print('The original list is : ' + str(test_list))
K = 1
res = []
for idx in range(0, len(test_list) - 1):
    res.append(abs(test_list[idx][K] - test_list[idx + 1][K]))
print('Resultant tuple list : ' + str(res))