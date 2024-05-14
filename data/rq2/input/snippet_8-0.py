def inset_element_list(lst, x, n):
    i = n
    while i < len(lst):
        lst.insert(i, x)
        i += n + 1
    return lst
print('Original list:')
print(nums)
x = 20
n = 4
print('\nInsert', x, 'in said list after every', n, 'th element:')
print(inset_element_list(nums, x, n))
chars = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
print('\nOriginal list:')
print(chars)
x = 'Z'
n = 3
print('\nInsert', x, 'in said list after every', n, 'th element:')
print(inset_element_list(chars, x, n))