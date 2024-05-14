def tuples_to_list_str(lst):
    result = [('%s ' * len(el) % el).strip() for el in lst]
    return result
print('Original list of tuples:')
print(colors)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_str(colors))
names = [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
print('\nOriginal list of tuples:')
print(names)
print('\nConvert the said list of tuples to a list of strings:')
print(tuples_to_list_str(names))