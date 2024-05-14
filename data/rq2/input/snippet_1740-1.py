def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res
test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
print('The original list is : ' + str(test_list))
res = prod([sub[K] for sub in test_list])
print('Product of Kth Column of Tuple List : ' + str(res))