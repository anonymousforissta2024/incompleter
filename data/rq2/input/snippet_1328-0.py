def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)
print('Original list of strings:')
print(colors)
print('\nConvert the said list of strings into list of lists:')
print(strings_to_listOflists(colors))