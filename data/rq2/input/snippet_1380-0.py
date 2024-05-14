def test(list1):
    result = [tuple((v for v in i if not isinstance(v, str))) for i in list1]
    return list(result)
print('\nOriginal list:')
print(marks)
print('\nRemove all strings from the said list of tuples:')
print(test(marks))