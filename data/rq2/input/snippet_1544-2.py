test_list = ['geeksforgeeks', 'best', 'geeks', 'and', 'geeks', 'love', 'CS']
print('The original list is : ' + str(test_list))
pref = 'geek'
for val in test_list:
    if val.startswith(pref):
        res.append([val])
    else:
        res[-1].append(val)
print('Prefix Split List : ' + str(res))