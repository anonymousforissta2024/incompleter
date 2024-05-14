import re
print('Original string:')
print(str1)
print('After removing lowercase letters, above string becomes:')
remove_lower = lambda text: re.sub('[a-z]', '', text)
result = remove_lower(str1)
print(result)