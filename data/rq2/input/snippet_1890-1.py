print('The original dictionary : ' + str(test_dict))
sub_list = ['love', 'good']
res = dict()
for key, val in test_dict.items():
    if not any((ele in val for ele in sub_list)):
        res[key] = val
print('Filtered Dictionary : ' + str(res))