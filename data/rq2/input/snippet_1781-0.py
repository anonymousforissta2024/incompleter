print('The original dictionary is : ' + str(test_dict))
res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])
print('The sorted dictionary : ' + str(res))