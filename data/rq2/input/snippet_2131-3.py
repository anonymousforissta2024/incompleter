test_list = ['Gfg', 'is', 'Best']
print('The original list : ' + str(test_list))
subs_dict = {'Gfg': [5, 6, 7], 'is': [7, 4, 2]}
res = [ele if ele not in subs_dict else subs_dict[ele][K] for ele in test_list]
print('The list after substitution : ' + str(res))