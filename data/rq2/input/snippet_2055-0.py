test_tup = (5, (6, (1, (9, (10, None)))))
print('The original tuple is : ' + str(test_tup))
while test_tup:
    res += test_tup[0]
    test_tup = test_tup[1]
print('Summation of 1st positions : ' + str(res))