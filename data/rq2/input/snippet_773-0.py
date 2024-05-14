def l_strs_to_l_chars(lst):
    result = [i for element in lst for i in element]
    return result
print('Original list:')
print(colors)
print('\nConvert the said list of strings and characters to a single list of characters:')
print(l_strs_to_l_chars(colors))