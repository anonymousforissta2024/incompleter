def concatenate_lists(l1, l2, l3):
    return [i + j + k for i, j, k in zip(l1, l2, l3)]
l1 = ['0', '1', '2', '3', '4']
l3 = ['100', '200', '300', '400', '500']
print('Original lists:')
print(l1)
print(l2)
print(l3)
print('\nConcatenate element-wise three said lists:')
print(concatenate_lists(l1, l2, l3))