print('The original list is : ' + str(test_list))
res = dict()
for sub in test_list:
    if len(sub) not in res:
        res[len(sub)] = 1
    else:
        res[len(sub)] += 1
print('Row length frequencies : ' + str(res))