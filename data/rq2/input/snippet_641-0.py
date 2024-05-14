from itertools import groupby

def compress(l_nums):
    return [key for key, group in groupby(l_nums)]
print('Original list:')
print(n_list)
print('\nAfter removing consecutive duplicates:')
print(compress(n_list))