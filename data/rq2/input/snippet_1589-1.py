test_tup = (5, 6, 7, 4, 9)
print('The original tuple is : ', test_tup)
res = [ele for sub in test_tup for ele in (sub, K)]
print('Converted Tuple with K : ', res)