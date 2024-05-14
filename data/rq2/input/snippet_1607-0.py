print('The original list : ' + str(test_list))
res = dict()
for idx in range(1, max(test_list)):
    res[idx] = 0
    for key in test_list:
        if key % idx == 0:
            res[idx] += 1
print('The constructed dictionary : ' + str(res))