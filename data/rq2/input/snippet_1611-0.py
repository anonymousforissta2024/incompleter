test_list1 = ['Gfg', 'is', 'not', 'best', 'and', 'not', 'for', 'CS']
test_list2 = ['Its ok', 'all ok', 'wrong', 'looks ok', 'ok', 'wrong', 'ok', 'thats ok']
print('The original list 1 is : ' + str(test_list1))
print('The original list 2 is : ' + str(test_list2))
sub_str = 'ok'
for ele1, ele2 in zip(test_list1, test_list2):
    if sub_str in ele2:
        res.append(ele1)
print('The extracted list : ' + str(res))