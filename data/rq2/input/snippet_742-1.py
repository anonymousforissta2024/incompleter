def split_two_parts(n_list, L):
    return (n_list[:L], n_list[L:])
print('Original list:')
print(n_list)
first_list_length = 3
print('\nLength of the first part of the list:', first_list_length)
print('\nSplited the said list into two parts:')
print(split_two_parts(n_list, first_list_length))