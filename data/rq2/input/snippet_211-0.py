def pair_consecutive_elements(lst):
    result = [[lst[i], lst[i + 1]] for i in range(len(lst) - 1)]
    return result
print('Original lists:')
print(nums)
print('Pair up the consecutive elements of the said list:')
print(pair_consecutive_elements(nums))
nums = [1, 2, 3, 4, 5]
print('\nOriginal lists:')
print(nums)
print('Pair up the consecutive elements of the said list:')
print(pair_consecutive_elements(nums))