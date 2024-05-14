print('The original tuple : ' + str(test_tup))
res = tuple((i * j for i, j in zip(test_tup, test_tup[1:])))
print('Resultant tuple after multiplication : ' + str(res))