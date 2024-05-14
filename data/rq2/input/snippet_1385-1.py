def max_min_sublist(lst):
    max_result = max(lst, key=sum)
    min_result = min(lst, key=sum)
    return (max_result, min_result)
nums = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print('Original list:')
print(nums)
print('\nMaximum sum of sub list of the said list of lists:')
print(result[0])
print('\nMinimum sum of sub list of the said list of lists:')
print(result[1])