test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
print('The original list is : ' + str(test_list))
res = 0
for ele in test_list:
    if ele.startswith(test_sub):
        res = res + 1
print('Strings count with matching frequency : ' + str(res))