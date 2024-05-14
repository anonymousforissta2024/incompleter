def test(keys, values):
    return dict(zip(keys, values))
l2 = [1, 2, 3, 4, 5]
print('Original lists:')
print(l1)
print(l2)
print('\nCombine the values of the said two lists into a dictionary:')
print(test(l1, l2))