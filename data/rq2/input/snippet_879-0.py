def common_in_nested_lists(nested_list):
    result = list(set.intersection(*map(set, nested_list)))
    return result
print('\nOriginal lists:')
print(nested_list)
print('\nCommon element(s) in nested lists:')
print(common_in_nested_lists(nested_list))