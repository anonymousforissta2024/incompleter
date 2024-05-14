def sort_numeric_strings(nums_str):
    result = sorted(nums_str, key=lambda el: int(el))
    return result
print('Original list:')
print(nums_str)
print('\nSort the said list of strings(numbers) numerically:')
print(sort_numeric_strings(nums_str))