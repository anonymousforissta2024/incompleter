def alternate_elements(list_data):
    result = []
    for item in list_data[::2]:
        result.append(item)
    return result
print('Original list:')
print(colors)
print('List with alternate elements from the said list:')
print(alternate_elements(colors))
nums = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
print('\nOriginal list:')
print(nums)
print('List with alternate elements from the said list:')
print(alternate_elements(nums))