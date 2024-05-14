def shift_first_last(lst):
    x = lst.pop(0)
    y = lst.pop()
    lst.insert(0, y)
    lst.insert(len(lst), x)
    return lst
print('Original list:')
print(nums)
print('Shift last element to first position and first element to last position of the said list:')
print(shift_first_last(nums))
chars = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
print('\nOriginal list:')
print(chars)
print('Shift last element to first position and first element to last position of the said list:')
print(shift_first_last(chars))