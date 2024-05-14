def insert_elemnt_nth(lst, ele, n):
    result = []
    for st_idx in range(0, len(lst), n):
        result.extend(lst[st_idx:st_idx + n])
        result.append(ele)
    result.pop()
    return result
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('Original list:')
print(nums)
i_ele_pos = 2
print('\nInsert', i_ele, 'in the said list after', i_ele_pos, 'nd element:')
print(insert_elemnt_nth(nums, i_ele, i_ele_pos))
i_ele = 'b'
i_ele_pos = 4
print('\nInsert', i_ele, 'in the said list after', i_ele_pos, 'th element:')
print(insert_elemnt_nth(nums, i_ele, i_ele_pos))