def tuples_to_list_str(lst):
    result = [('%s ' * len(el) % el).strip() for el in lst]
    return result
colors = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
print('Original list of tuples:')
print(colors)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_str(colors))
print('\nOriginal list of tuples:')
print(names)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_str(names))