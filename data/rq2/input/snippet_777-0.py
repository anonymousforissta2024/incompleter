import re
print('Original string:')
print(txt)
new_txt = re.sub('(?<=\\d)\\s(?=\\d)', '', txt)
print('\nAfter concatenating the consecutive numbers in the said string:')
print(new_txt)