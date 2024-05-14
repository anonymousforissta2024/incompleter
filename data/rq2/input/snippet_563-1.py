def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result
print('Original list of tuples:')
print(colors)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_string(colors))
names = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]
print('\nOriginal list of tuples:')
print(names)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_string(names))