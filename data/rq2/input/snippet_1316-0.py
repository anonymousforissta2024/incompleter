def sort_numeric_strings(nums_str):
    result = [int(x) for x in nums_str]
    result.sort()
    return result
print('Original list:')
print(nums_str)
print('\nSort the said list of strings(numbers) numerically:')
print(sort_numeric_strings(nums_str))