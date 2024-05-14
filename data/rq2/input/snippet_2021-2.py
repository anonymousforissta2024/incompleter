from itertools import permutations
test_list = ['geeks4u', 'allbest', 'abcdef']
print('The original list : ' + str(test_list))
substr_list = ['s4u', 'est', 'al', 'ge', 'ek', 'def', 'lb']
K = 3
res = []
for ele in perms:
    if ele in test_list:
        res.append(ele)
print('Strings after joins : ' + str(res))