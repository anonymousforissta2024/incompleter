test_list = ['Gfg is good', 'for Geeks', 'I love Gfg', 'Its useful']
K = 'Gfg'
print('The original list : ' + str(test_list))
for idx, ele in enumerate(test_list):
    if K in ele:
        res.append(idx)
print('The indices list : ' + str(res))