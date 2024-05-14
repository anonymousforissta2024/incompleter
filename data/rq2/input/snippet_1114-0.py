def unicode_to_str(lst):
    result = [str(x) for x in lst]
    return result
print('Original lists:')
print(students)
print(' Convert the said unicode list to a list contains strings:')
print(unicode_to_str(students))