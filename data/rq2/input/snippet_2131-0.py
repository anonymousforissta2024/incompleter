test_list = ['Gfg', 'is', 'Best']
print('The original list : ' + str(test_list))
K = 2
res = [ele if ele not in subs_dict else subs_dict[ele][K] for ele in test_list]
print('The list after substitution : ' + str(res))