def test(dictionary):
    dictionary['Math'] = [x + 1 for x in dictionary['Math']]
    dictionary['Physics'] = [x - 2 for x in dictionary['Physics']]
    return dictionary
print('\nOriginal Dictionary:')
print(dictionary)
print('\nUpdate the list values of the said dictionary:')
print(test(dictionary))