def sort_mixed_list(mixed_list):
    int_part = sorted([i for i in mixed_list if type(i) is int])
    str_part = sorted([i for i in mixed_list if type(i) is str])
    return int_part + str_part
print('Original list:')
print(mixed_list)
print('\nSort the said  mixed list of integers and strings:')
print(sort_mixed_list(mixed_list))