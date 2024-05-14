test_list = [[5, 8], [2, 0], [5, 4], [2, 3], [7, 9]]
print('The original list : ' + str(test_list))
for idx in test_list:
    res[idx[0]].append(idx[1])
print('The Grouped Matrix : ' + str(res))