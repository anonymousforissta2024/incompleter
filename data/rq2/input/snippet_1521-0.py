print('The original list is : ' + str(test_list))
res = {}
max_len = 0
for ele in test_list:
    if len(ele) > max_len:
        res = ele
        max_len = len(ele)
print('Maximum keys Dictionary : ' + str(res))