print('The original list : ' + str(test_list))
res = []
temp = set()
for inner in test_list:
    for ele in inner:
        if not ele in temp:
            temp.add(ele)
            res.append(ele)
print('Unique elements in nested tuples are : ' + str(res))