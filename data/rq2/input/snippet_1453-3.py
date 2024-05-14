def insert_spec_position(x, n_list, pos):
    return n_list[:pos - 1] + [x] + n_list[pos - 1:]
print('Original list:')
print(n_list)
kth_position = 3
x = 12
result = insert_spec_position(x, n_list, kth_position)
print('\nAfter inserting an element at kth position in the said list:')
print(result)