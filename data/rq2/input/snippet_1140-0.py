def find_substring(str1, sub_str):
    if any((sub_str in s for s in str1)):
        return True
    return False
print('Original list:')
print(colors)
sub_str = 'ack'
print('Substring to search:')
print(sub_str)
print('Check if a substring presents in the said list of string values:')
print(find_substring(colors, sub_str))
sub_str = 'abc'
print('Substring to search:')
print(sub_str)
print('Check if a substring presents in the said list of string values:')
print(find_substring(colors, sub_str))