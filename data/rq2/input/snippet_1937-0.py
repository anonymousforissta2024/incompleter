print('The original list is : ' + str(test_list))
test_dict = {'gfg': 5, 'is': 10, 'best': 13, 'for': 2, 'geeks': 15}
res = []
for sub in test_list:
    sum = 0
    for val in sub:
        if val in test_dict:
            sum += test_dict[val]
    res.append(sum)
print('The Row scores : ' + str(res))