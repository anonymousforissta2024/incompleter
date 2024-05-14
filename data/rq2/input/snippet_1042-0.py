def check_element_in_list(lst, x, n):
    t = 0
    try:
        for _ in range(n):
            t = lst.index(x, t) + 1
        return True
    except ValueError:
        return False
print('Original list:')
print(nums)
x = 3
n = 4
print('\nCheck if', x, 'occurs at least', n, 'times in a list:')
print(check_element_in_list(nums, x, n))
x = 0
n = 5
print('\nCheck if', x, 'occurs at least', n, 'times in a list:')
print(check_element_in_list(nums, x, n))
x = 8
n = 3
print('\nCheck if', x, 'occurs at least', n, 'times in a list:')
print(check_element_in_list(nums, x, n))