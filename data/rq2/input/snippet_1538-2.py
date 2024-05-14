test_list = ['geekforgeeks', [5, 4, 3, 4], 'is', ['best', 'good', 'better', 'average']]
print('The original list is : ' + str(test_list))
K = 4
cnt = 0
while cnt <= K - 1:
    temp = []
    for idx in test_list:
        if not isinstance(idx, list):
            temp.append(idx)
        else:
            temp.append(idx[cnt])
    cnt += 1
    res.append(temp)
print('All index Combinations : ' + str(res))