def reverse_strings_list(string_list):
    result = list(map(lambda x: ''.join(reversed(x)), string_list))
    return result
print('\nOriginal lists:')
print(colors_list)
print('\nReverse strings of the said given list:')
print(reverse_strings_list(colors_list))