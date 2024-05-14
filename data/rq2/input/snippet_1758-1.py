test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
print('The original list is : ' + str(test_list))
for sub in test_list:
    res[tuple(sub[:2])] = tuple(sub[2:])
print('The mapped Dictionary : ' + str(res))