def extract_string(str_list1, l):
    result = list(filter(lambda e: len(e) == l, str_list1))
    return result
str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
print('Original list:')
print(str_list1)
print('\nlength of the string to extract:')
print(l)
print('\nAfter extracting strings of specified length from the said list:')
print(extract_string(str_list1, l))