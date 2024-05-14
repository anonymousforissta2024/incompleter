def remove_list_range(input_list, left_range, rigth_range):
    result = [i for i in input_list if min(i) >= left_range and max(i) <= rigth_range]
    return result
list1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
left_range = 13
print('Original list:')
print(list1)
print('\nAfter removing sublists from a given list of lists, which contains an element outside the given range:')
print(remove_list_range(list1, left_range, rigth_range))