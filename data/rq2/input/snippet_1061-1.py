def index_on_inner_list(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Original lists:')
print('list1:', list1)
print('list2:', list2)
print("\nRemove all elements from 'list1' present in 'list2:")
print(index_on_inner_list(list1, list2))