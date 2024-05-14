from itertools import groupby

def pack_consecutive_duplicates(l_nums):
    return [list(group) for key, group in groupby(l_nums)]
print('Original list:')
print(n_list)
print('\nAfter packing consecutive duplicates of the said list elements into sublists:')
print(pack_consecutive_duplicates(n_list))