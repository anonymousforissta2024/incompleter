def position_max_min(nums):
    max_val = max(nums)
    min_val = min(nums)
    max_result = [i for i, j in enumerate(nums) if j == max_val]
    min_result = [i for i, j in enumerate(nums) if j == min_val]
    return (max_result, min_result)
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
print('Original list:')
print(nums)
print('\nIndex positions of the maximum value of the said list:')
print(result[0])
print('\nIndex positions of the minimum value of the said list:')
print(result[1])