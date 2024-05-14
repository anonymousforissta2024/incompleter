test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]
print('The original list : ' + str(test_list))
temp = set()
for inner in test_list:
    for ele in inner:
        if not ele in temp:
            temp.add(ele)
            res.append(ele)
print('Unique elements in nested tuples are : ' + str(res))