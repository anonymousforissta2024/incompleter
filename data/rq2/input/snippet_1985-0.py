print('The original dictionary is : ' + str(test_dict))
res = [(key, tuple((sub[key] for sub in test_dict.values()))) for key in test_dict['gfg']]
print('The grouped dictionary : ' + str(res))