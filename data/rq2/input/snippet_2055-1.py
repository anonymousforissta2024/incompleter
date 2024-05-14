print('The original tuple is : ' + str(test_tup))
res = 0
while test_tup:
    res += test_tup[0]
    test_tup = test_tup[1]
print('Summation of 1st positions : ' + str(res))