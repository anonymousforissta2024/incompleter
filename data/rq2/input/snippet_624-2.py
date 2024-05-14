list2 = [[2, 4], [6, 8], [10, 12, 14]]
print('Original lists:')
print(list1)
print(list2)
result = list(map(list.__add__, list1, list2))
print('\nZipped list:\n' + str(result))