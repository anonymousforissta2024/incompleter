print('The original string is : ' + str(test_str))
repl_dict = {'Gfg': 'It', 'Classes': 'They'}
test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)
print('The string after replacing : ' + str(res))