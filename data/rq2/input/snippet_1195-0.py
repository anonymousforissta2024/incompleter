def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=lambda x: x[index_no])
    return result
print('Original list:')
print(students)
index_no = 0
print('\nSort the said list of lists by a given index', '( Index = ', index_no, ') of the inner list')
print(index_on_inner_list(students, index_no))
index_no = 2
print('\nSort the said list of lists by a given index', '( Index = ', index_no, ') of the inner list')
print(index_on_inner_list(students, index_no))