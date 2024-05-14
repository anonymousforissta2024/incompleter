test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]
print('The original list is : ' + str(test_list))
res = {(a, b) for a, b in temp if a < b}
print('The Symmetric tuples : ' + str(res))