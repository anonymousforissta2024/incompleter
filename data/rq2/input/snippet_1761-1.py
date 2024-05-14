test_list1 = ['Gfg', 'is', 'Best']
test_list2 = ['I love Gfg', 'Its Best for Geeks', 'Gfg means CS']
print('The original list 1 : ' + str(test_list1))
print('The original list 2 : ' + str(test_list2))
for ele in test_list1:
    temp = False
    for sub in test_list2:
        if ele in sub:
            temp = True
            break
    res.append(temp)
print('The match list : ' + str(res))