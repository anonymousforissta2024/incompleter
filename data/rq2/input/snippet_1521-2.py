test_list = [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4}, {'gfg': 2}]
print('The original list is : ' + str(test_list))
res = {}
for ele in test_list:
    if len(ele) > max_len:
        res = ele
        max_len = len(ele)
print('Maximum keys Dictionary : ' + str(res))