test_dict = {'Gfg': 2, 'is': 4, 'Best': 6}
K = 'Gfg'
print('The original list : ' + str(test_list))
print('The original Dictionary : ' + str(test_dict))
res = None
if all((K in sub for sub in [test_dict, test_list])):
    res = test_dict[K]
print('Extracted Value : ' + str(res))