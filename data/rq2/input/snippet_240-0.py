def position_max_min(nums):
    max_val = max(nums)
    min_val = min(nums)
    max_result = [i for i, j in enumerate(nums) if j == max_val]
    min_result = [i for i, j in enumerate(nums) if j == min_val]
    return (max_result, min_result)
print('Original list:')
print(nums)
result = position_max_min(nums)
print('\nIndex positions of the maximum value of the said list:')
print(result[0])
print('\nIndex positions of the minimum value of the said list:')
print(result[1])