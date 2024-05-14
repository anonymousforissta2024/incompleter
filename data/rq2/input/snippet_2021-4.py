from itertools import permutations
print('The original list : ' + str(test_list))
substr_list = ['s4u', 'est', 'al', 'ge', 'ek', 'def', 'lb']
K = 3
perms = list(set(map(''.join, permutations(substr_list, r=K))))
res = []
for ele in perms:
    if ele in test_list:
        res.append(ele)
print('Strings after joins : ' + str(res))