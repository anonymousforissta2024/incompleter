test_dict = {1: 'Gfg is best for geeks', 2: 'Gfg is good', 3: 'I love Gfg'}
print('The original dictionary : ' + str(test_dict))
sub_list = ['love', 'good']
for key, val in test_dict.items():
    if not any((ele in val for ele in sub_list)):
        res[key] = val
print('Filtered Dictionary : ' + str(res))