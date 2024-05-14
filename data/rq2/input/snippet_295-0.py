def cyclically_iteration(lst, spec_index):
    result = []
    length = len(lst)
    for i in range(length):
        element_index = spec_index % length
        result.append(lst[element_index])
        spec_index += 1
    return result
print('Original list:')
print(chars)
spec_index = 3
print('\nIterate the said  list cyclically on specific index position', spec_index, ':')
print(cyclically_iteration(chars, spec_index))
spec_index = 5
print('\nIterate the said  list cyclically on specific index position', spec_index, ':')
print(cyclically_iteration(chars, spec_index))