import re
str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
print('Original string:')
print(str1)
print('After removing lowercase letters, above string becomes:')
remove_lower = lambda text: re.sub('[a-z]', '', text)
print(result)