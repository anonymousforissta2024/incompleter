from itertools import permutations
test_list = ['geeks4u', 'allbest', 'abcdef']
print('The original list : ' + str(test_list))
K = 3
perms = list(set(map(''.join, permutations(substr_list, r=K))))
res = []
for ele in perms:
    if ele in test_list:
        res.append(ele)
print('Strings after joins : ' + str(res))