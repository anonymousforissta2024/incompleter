def common_list_of_lists(lst):
    temp = set(lst[0]).intersection(*lst)
    return list(temp)
print('Original list:')
print(nums)
print('\nCommon elements of the said list of lists:')
print(common_list_of_lists(nums))
chars = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
print('\nOriginal list:')
print(chars)
print('\nCommon elements of the said list of lists:')
print(common_list_of_lists(chars))