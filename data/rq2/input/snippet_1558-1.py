print('The original dictionary is : ' + str(test_dict))
res = []
for key, val in test_dict.items():
    res.append([key] + val)
print('The converted list is : ' + str(res))