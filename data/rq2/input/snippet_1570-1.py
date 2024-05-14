print('The original list is : ' + str(test_list))
res = tuple((tuple(sub) for sub in test_list))
print('The converted data : ' + str(res))