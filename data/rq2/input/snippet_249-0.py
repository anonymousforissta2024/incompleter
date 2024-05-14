def sort_sublists(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result
print('Original list:')
print(list1)
print('\nSort the list of lists by length and value:')
print(sort_sublists(list1))