print('The original tuple is : ' + str(test_tup))
res = int(''.join((str(ele) for ele in test_tup)), 2)
print('Decimal number is : ' + str(res))