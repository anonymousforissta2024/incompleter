print('The original list : ' + str(test_list))
res = ' '.join([idx for tup in test_list for idx in tup])
print('Tuple list converted to String is : ' + res)