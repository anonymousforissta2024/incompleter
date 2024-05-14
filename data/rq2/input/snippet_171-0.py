def unique_sublists(input_list):
    result = {}
    for l in input_list:
        result.setdefault(tuple(l), list()).append(1)
    for a, b in result.items():
        result[a] = sum(b)
    return result
print('Original list:')
print(list1)
print('Number of unique lists of the said list:')
print(unique_sublists(list1))
color1 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
print('\nOriginal list:')
print(color1)
print('Number of unique lists of the said list:')
print(unique_sublists(color1))