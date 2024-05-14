def remove_last_n(nums, N):
    result = nums[:len(nums) - N]
    return result
print('Original lists:')
print(nums)
N = 3
print('\nRemove the last', N, 'elements from the said list:')
print(remove_last_n(nums, N))
N = 5
print('\nRemove the last', N, 'elements from the said list:')
print(remove_last_n(nums, N))
N = 1
print('\nRemove the last', N, 'element from the said list:')
print(remove_last_n(nums, N))