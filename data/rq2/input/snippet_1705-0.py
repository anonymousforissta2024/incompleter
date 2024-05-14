print('The original tuple : ' + str(test_tup))
res = tuple()
for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
        res = res + (ele,)
print('Elements after removal of nested records : ' + str(res))