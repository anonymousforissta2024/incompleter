print('The original list : ' + str(test_list))
res = {idx[0]: [] for idx in test_list}
for idx in test_list:
    res[idx[0]].append(idx[1])
print('The Grouped Matrix : ' + str(res))