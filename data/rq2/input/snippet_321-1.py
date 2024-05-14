print('Original list:')
print(list1)
print('\nAfter deleting the empty lists from the said lists of lists')
list2 = [x for x in list1 if x]
print(list2)