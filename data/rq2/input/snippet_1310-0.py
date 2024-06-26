def flatten_list(n_list):
    result_list = []
    if not n_list:
        return result_list
    stack = [list(n_list)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num:
            stack.append(c_num)
        if isinstance(next, list):
            if next:
                stack.append(list(next))
        else:
            result_list.append(next)
    result_list.reverse()
    return result_list
print('Original list:')
print(n_list)
print('\nFlatten list:')
print(flatten_list(n_list))