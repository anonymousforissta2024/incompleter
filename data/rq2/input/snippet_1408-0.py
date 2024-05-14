from itertools import product

def permutations_colors(inp, n):
    for x in product(inp, repeat=n):
        c = ''.join(x)
        print(c, end=', ')
str1 = 'Red'
print('Original String: ', str1)
print('Permutations of specified elements, drawn from specified values:')
print('\nn = 1')
permutations_colors(str1, n)
n = 2
print('\nn = 2')
permutations_colors(str1, n)
n = 3
print('\nn = 3')
permutations_colors(str1, n)
lst1 = ['Red', 'Green', 'Black']
print('\n\nOriginal list: ', lst1)
print('Permutations of specified elements, drawn from specified values:')
n = 1
print('\nn = 1')
permutations_colors(lst1, n)
n = 2
print('\nn = 2')
permutations_colors(lst1, n)
n = 3
print('\nn = 3')
permutations_colors(lst1, n)