test_list = [[4, 5, 6], [6, 7, 3], [1, 3, 4]]
print('The original list is : ' + str(test_list))
res = []
for idx, ele in zip(add_list, test_list):
    for e in ele:
        res.append((idx, e))
print('Matrix after conversion : ' + str(res))