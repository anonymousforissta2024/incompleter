def inset_element_list(lst, x, n):
    i = n
    while i < len(lst):
        lst.insert(i, x)
        i += n + 1
    return lst
nums = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
print('Original list:')
print(nums)
x = 20
print('\nInsert', x, 'in said list after every', n, 'th element:')
print(inset_element_list(nums, x, n))
chars = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
print('\nOriginal list:')
print(chars)
x = 'Z'
n = 3
print('\nInsert', x, 'in said list after every', n, 'th element:')
print(inset_element_list(chars, x, n))