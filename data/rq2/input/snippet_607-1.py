def remove_kth_element(n_list, L):
    return n_list[:L - 1] + n_list[L:]
n_list = [1, 1, 2, 3, 4, 4, 5, 1]
print('Original list:')
print(n_list)
kth_position = 3
print('\nAfter removing an element at the kth position of the said list:')
print(result)