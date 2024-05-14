def flatten(test_tuple):
    for tup in test_tuple:
        if isinstance(tup, tuple):
            yield from flatten(tup)
        else:
            yield tup
print('The original tuple : ' + str(test_tuple))
res = {}
for ele in flatten(test_tuple):
    if ele not in res:
        res[ele] = 0
    res[ele] += 1
print('The elements frequency : ' + str(res))