def count_element_in_list(input_list, x):
    ctr = 0
    for i in range(len(input_list)):
        if x in input_list[i]:
            ctr += 1
    return ctr
print('Original list:')
print(list1)
print('\nCount 1 in the said list:')
print(count_element_in_list(list1, 1))
print('\nCount 7 in the said list:')
print(count_element_in_list(list1, 7))
list1 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
print('\nOriginal list:')
print(list1)
print("\nCount 'A' in the said list:")
print(count_element_in_list(list1, 'A'))
print("\nCount 'E' in the said list:")
print(count_element_in_list(list1, 'E'))