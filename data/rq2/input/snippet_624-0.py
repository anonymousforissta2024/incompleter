list1 = [[1, 3], [5, 7], [9, 11]]
print('Original lists:')
print(list1)
print(list2)
result = list(map(list.__add__, list1, list2))
print('\nZipped list:\n' + str(result))