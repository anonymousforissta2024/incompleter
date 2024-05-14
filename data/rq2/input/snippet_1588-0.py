print('The original list is : ' + str(test_list))
ele = 3
K = 1
res = []
for x, y, z in test_list:
    if y == ele:
        res.append((x, y, z))
print('The tuples of element at Kth position : ' + str(res))