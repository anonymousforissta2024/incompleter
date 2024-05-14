def count_integer(list1):
    ctr = 0
    for i in list1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr
print('Original list:')
print(list1)
print('\nNumber of integers in the said mixed list:')
print(count_integer(list1))