test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]
print('The original list is : ' + str(test_list))
temp = set(test_list) & {(b, a) for a, b in test_list}
print('The Symmetric tuples : ' + str(res))