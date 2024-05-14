from collections import defaultdict
print('The original tuple is : ' + str(test_tup))
res = defaultdict(int)
for ele in test_tup:
    res[ele] += 1
print('Tuple elements frequency is : ' + str(dict(res)))