from itertools import combinations
print('The original list : ' + str(test_list))
res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]
print('The Summation combinations are : ' + str(res))