def check_element_in_list(lst, x, n):
    t = 0
    try:
        for _ in range(n):
            t = lst.index(x, t) + 1
        return True
    except ValueError:
        return False
nums = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
print('Original list:')
print(nums)
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