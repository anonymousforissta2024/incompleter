def max_min_list_tuples(nums):
    zip(*nums)
    result1 = map(max, zip(*nums))
    result2 = map(min, zip(*nums))
    return (list(result1), list(result2))
nums = [(2, 3), (2, 4), (0, 6), (7, 1)]
print('Original list:')
print(nums)
print('\nMaximum value  for each tuple position in the said list of tuples:')
print(result[0])
print('\nMinimum value  for each tuple position in the said list of tuples:')
print(result[1])