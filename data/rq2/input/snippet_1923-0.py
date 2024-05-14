test_list = [8, 3, 2]
print('The original dictionary is : ' + str(test_dict))
print('The original list is : ' + str(test_list))
res = {}
for key, ele in zip(test_list, test_dict.items()):
    res[key] = dict([ele])
print('The mapped dictionary : ' + str(res))