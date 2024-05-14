from itertools import chain
print('The original list is : ' + str(test_list))
temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
    for ele in sub:
        res.add(ele)
print('The extracted digits : ' + str(res))