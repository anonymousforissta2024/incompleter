def delete_all_occurrences(str1, ch):
    result = str1.replace(ch, '')
    return result
print('Original string:')
print(str_text)
print('\nModified string:')
ch = 'a'
print(delete_all_occurrences(str_text, ch))