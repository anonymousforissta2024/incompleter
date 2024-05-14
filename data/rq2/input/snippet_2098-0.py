print('The original dictionary is : ' + str(test_dict))
key = 'Himani'
res = None
res_max = 0
for sub in test_dict:
    if test_dict[sub][key] > res_max:
        res_max = test_dict[sub][key]
        res = sub
print('The required key is : ' + str(res))