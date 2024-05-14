K = 'Gfg'
print('The original list : ' + str(test_list))
res = []
for idx, ele in enumerate(test_list):
    if K in ele:
        res.append(idx)
print('The indices list : ' + str(res))