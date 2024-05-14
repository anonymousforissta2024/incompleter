def extract_string(str_list1, l):
    result = [e for e in str_list1 if len(e) == l]
    return result
str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
print('Original list:')
print(str_list1)
print('\nlength of the string to extract:')
print(l)
print('\nAfter extracting strings of specified length from the said list:')
print(extract_string(str_list1, l))