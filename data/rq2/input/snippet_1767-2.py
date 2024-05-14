test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
print('The original list is : ' + str(test_list))
K = 1
for idx in range(0, len(test_list) - 1):
    res.append(abs(test_list[idx][K] - test_list[idx + 1][K]))
print('Resultant tuple list : ' + str(res))