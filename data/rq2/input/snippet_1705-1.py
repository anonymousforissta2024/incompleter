test_tup = (1, 5, 7, (4, 6), 10)
print('The original tuple : ' + str(test_tup))
for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
        res = res + (ele,)
print('Elements after removal of nested records : ' + str(res))