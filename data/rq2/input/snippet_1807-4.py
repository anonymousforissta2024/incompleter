test_dict = {'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'geeks': 5, 'CS': 6}
print('The original dictionary is : ' + str(test_dict))
K = 2
res = []
count = 0
flag = 0
for key in test_dict:
    indict[key] = test_dict[key]
    count += 1
    if count % K == 0 and flag:
        res.append(indict)
        indict = dict()
        count = 0
    flag = 1
print('The converted list : ' + str(res))