def unique_values_in_list_of_lists(lst):
    result = set((x for l in lst for x in l))
    return list(result)
print('Original list:')
print(nums)
print('Unique values of the said list of lists:')
print(unique_values_in_list_of_lists(nums))
chars = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
print('\nOriginal list:')
print(chars)
print('Unique values of the said list of lists:')
print(unique_values_in_list_of_lists(chars))