def max_min_sublist(lst):
    max_result = max(lst, key=sum)
    min_result = min(lst, key=sum)
    return (max_result, min_result)
print('Original list:')
print(nums)
result = max_min_sublist(nums)
print('\nMaximum sum of sub list of the said list of lists:')
print(result[0])
print('\nMinimum sum of sub list of the said list of lists:')
print(result[1])