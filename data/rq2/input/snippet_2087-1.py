def grp_ele(test_list1, test_list2):
    temp = []
    for i in test_list1:
        if i in test_list2:
            if temp:
                yield temp
                temp = []
            yield i
        else:
            temp.append(i)
    if temp:
        yield temp
test_list2 = [9, 11]
print('The original list 1 is : ' + str(test_list1))
print('The original list 2 is : ' + str(test_list2))
res = list(grp_ele(test_list1, test_list2))
print('The Grouped list is : ' + str(res))