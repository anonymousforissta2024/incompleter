def strings_to_listOflists(colors):
    result = [list(word) for word in colors]
    return result
print('Original list of strings:')
print(colors)
print('\nConvert the said list of strings into list of lists:')
print(strings_to_listOflists(colors))