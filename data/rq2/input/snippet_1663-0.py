print('The original list is : ' + str(test_list))
add_list = ['Gfg', 'is', 'best']
res = []
for idx, ele in zip(add_list, test_list):
    for e in ele:
        res.append((idx, e))
print('Matrix after conversion : ' + str(res))