test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
print('The original list : ' + str(test_list))
for idx in range(1, max(test_list)):
    res[idx] = 0
    for key in test_list:
        if key % idx == 0:
            res[idx] += 1
print('The constructed dictionary : ' + str(res))