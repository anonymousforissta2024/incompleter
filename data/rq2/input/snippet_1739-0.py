print('The original list is : ' + str(test_list))
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
print('List after performing character swaps : ' + str(res))