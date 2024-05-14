def alternate_elements(list_data):
    result = []
    for item in list_data[::2]:
        result.append(item)
    return result
colors = ['red', 'black', 'white', 'green', 'orange']
print('Original list:')
print(colors)
print('List with alternate elements from the said list:')
print(alternate_elements(colors))
print('\nOriginal list:')
print(nums)
print('List with alternate elements from the said list:')
print(alternate_elements(nums))