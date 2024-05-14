def count_integer(list1):
    ert = list(map(lambda i: isinstance(i, float), list1))
    result = len([e for e in ert if e])
    return result
print('Original list:')
print(list1)
print('\nNumber of floats in the said mixed list:')
print(count_integer(list1))