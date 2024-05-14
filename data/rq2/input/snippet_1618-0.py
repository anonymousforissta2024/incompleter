test_list = [[6, 3, 1], [8, 9], [2], [10, 12, 7], [4, 11]]
print('The original list is : ' + str(test_list))
for sub in test_list:
    if len(sub) not in res:
        res[len(sub)] = 1
    else:
        res[len(sub)] += 1
print('Row length frequencies : ' + str(res))