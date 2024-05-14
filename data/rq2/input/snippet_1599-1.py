print('The original string is : ' + test_str)
sub_list = ['best', 'all']
for sub in sub_list:
    test_str = test_str.replace(' ' + sub + ' ', ' ')
print('The string after substring removal : ' + test_str)