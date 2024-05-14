test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
print('The original list is : ' + str(test_list))
res = len([i for i in test_list if subs in i])
print('All strings count with given substring are : ' + str(res))