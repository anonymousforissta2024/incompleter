def sort_mixed_list(mixed_list):
    mixed_list.sort(key=lambda e: (isinstance(e, str), e))
    return mixed_list
print('Original list:')
print(mixed_list)
print('\nSort the said  mixed list of integers and strings:')
print(sort_mixed_list(mixed_list))