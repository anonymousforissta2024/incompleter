def common_list_of_lists(lst):
    temp = set(lst[0]).intersection(*lst)
    return list(temp)
nums = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
print('Original list:')
print(nums)
print('\nCommon elements of the said list of lists:')
print(common_list_of_lists(nums))
print('\nOriginal list:')
print(chars)
print('\nCommon elements of the said list of lists:')
print(common_list_of_lists(chars))