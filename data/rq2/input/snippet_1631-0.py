print('The original dictionary is : ' + str(test_dict))
res = list(sorted({ele for val in test_dict.values() for ele in val}))
print('The unique values list is : ' + str(res))