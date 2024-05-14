print('The original list : ' + str(test_list))
K = 'Gfg'
idx = 2
res = sorted(test_list, key=lambda ele: ele[K][idx])
print('The required sort order : ' + str(res))