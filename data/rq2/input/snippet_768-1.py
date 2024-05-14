def shift_first_last(lst):
    x = lst.pop(0)
    y = lst.pop()
    lst.insert(0, y)
    lst.insert(len(lst), x)
    return lst
nums = [1, 2, 3, 4, 5, 6, 7]
print('Original list:')
print(nums)
print('Shift last element to first position and first element to last position of the said list:')
print(shift_first_last(nums))
print('\nOriginal list:')
print(chars)
print('Shift last element to first position and first element to last position of the said list:')
print(shift_first_last(chars))