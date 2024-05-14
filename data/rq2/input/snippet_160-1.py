def remove_chars(str1, unwanted_chars):
    for i in unwanted_chars:
        str1 = str1.replace(i, '')
    return str1
str2 = 'A%^!B#*CD'
unwanted_chars = ['#', '*', '!', '^', '%']
print('Original String : ' + str1)
print('After removing unwanted characters:')
print(remove_chars(str1, unwanted_chars))
print('\nOriginal String : ' + str2)
print('After removing unwanted characters:')
print(remove_chars(str2, unwanted_chars))