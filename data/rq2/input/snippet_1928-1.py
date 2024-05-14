test_list1 = ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
test_list2 = [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
print('The original list 1 is : ' + str(test_list1))
print('The original list 2 is : ' + str(test_list2))
for key, val in sub.items():
    for idx, ele in enumerate(test_list1):
        if key in ele:
            test_list1[idx] = ele.replace(key, val)
print('The list after replacement : ' + str(test_list1))