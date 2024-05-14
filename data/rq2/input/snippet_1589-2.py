print('The original tuple is : ', test_tup)
K = 'Gfg'
res = [ele for sub in test_tup for ele in (sub, K)]
print('Converted Tuple with K : ', res)