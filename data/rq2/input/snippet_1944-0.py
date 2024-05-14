def get_idx_ele_count(row):
    return len([ele for idx, ele in enumerate(row) if ele == idx])
print('The original list is : ' + str(test_list))
test_list.sort(key=get_idx_ele_count)
print('Sorted List : ' + str(test_list))