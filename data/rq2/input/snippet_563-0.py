def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print('Original list of tuples:')
print(colors)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_string(colors))
print('\nOriginal list of tuples:')
print(names)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_string(names))