test_dict = {'gfg': {'Manjeet': 5, 'Himani': 10}, 'is': {'Manjeet': 8, 'Himani': 9}, 'best': {'Manjeet': 10, 'Himani': 15}}
print('The original dictionary is : ' + str(test_dict))
key = 'Himani'
res = None
for sub in test_dict:
    if test_dict[sub][key] > res_max:
        res_max = test_dict[sub][key]
        res = sub
print('The required key is : ' + str(res))