test_str = 'geekforgeeks best for geeks'
print('The original string is : ' + str(test_str))
lookp_dict = {'best': 'good and better', 'geeks': 'all CS aspirants'}
temp = test_str.split()
for wrd in temp:
    res.append(lookp_dict.get(wrd, wrd))
res = ' '.join(res)
print('Replaced Strings : ' + str(res))