def test(lst):
    result = []
    for i in lst:
        j = i.replace(' ', '')
        result.append(j)
    return result
print('\nOriginal list:')
print(text)
print('Remove additional spaces from the said list:')
print(test(text))