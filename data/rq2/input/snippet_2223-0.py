def length(lst):
    if not lst:
        return 0
    return 1 + length(lst[1::2]) + length(lst[2::2])
print('Length of the string is: ')
print(a)