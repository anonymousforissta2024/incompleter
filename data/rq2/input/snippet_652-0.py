def delete_all_occurrences(str1, ch):
    result = str1.replace(ch, '')
    return result
str_text = 'Delete all occurrences of a specified character in a given string'
print('Original string:')
print(str_text)
print('\nModified string:')
print(delete_all_occurrences(str_text, ch))