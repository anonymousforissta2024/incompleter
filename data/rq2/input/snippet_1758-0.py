print('The original list is : ' + str(test_list))
res = dict()
for sub in test_list:
    res[tuple(sub[:2])] = tuple(sub[2:])
print('The mapped Dictionary : ' + str(res))