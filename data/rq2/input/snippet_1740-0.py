def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res
print('The original list is : ' + str(test_list))
K = 2
res = prod([sub[K] for sub in test_list])
print('Product of Kth Column of Tuple List : ' + str(res))