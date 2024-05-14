def sort_sublists(input_list):
    input_list.sort()
    input_list.sort(key=len)
    return input_list
print('Original list:')
print(list1)
print('\nSort the list of lists by length and value:')
print(sort_sublists(list1))