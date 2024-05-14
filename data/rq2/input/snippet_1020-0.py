def test(lst):
    return [lst for lst in lst if isinstance(lst, int)]
print('Original list:', mixed_list)
print('After removing all the values except integer values from the said array of mixed values:')
print(test(mixed_list))