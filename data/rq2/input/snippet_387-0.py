def relative_order(lst):
    result = [i for i in range(len(lst)) if lst[i] == None]
    return result
print('Original list:')
print(nums)
print('\nIndexes of all None items of the list:')
print(relative_order(nums))