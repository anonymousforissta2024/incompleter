test_list = [{'Gfg': [6, 7, 8], 'is': 9, 'best': 10}, {'Gfg': [2, 0, 3], 'is': 11, 'best': 19}, {'Gfg': [4, 6, 9], 'is': 16, 'best': 1}]
print('The original list : ' + str(test_list))
K = 'Gfg'
res = sorted(test_list, key=lambda ele: ele[K][idx])
print('The required sort order : ' + str(res))