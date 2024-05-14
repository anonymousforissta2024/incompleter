test_dict = {'Gfg': 4, 'is': 5, 'best': 9}
test_list = [8, 3, 2]
print('The original dictionary is : ' + str(test_dict))
print('The original list is : ' + str(test_list))
for key, ele in zip(test_list, test_dict.items()):
    res[key] = dict([ele])
print('The mapped dictionary : ' + str(res))