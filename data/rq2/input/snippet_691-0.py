def test(dictionary):
    for key in dictionary:
        dictionary[key].clear()
    return dictionary
print('\nOriginal Dictionary:')
print(dictionary)
print('\nClear the list values in the said dictionary:')
print(test(dictionary))