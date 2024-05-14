print('The original list is : ' + str(test_list))
K = 6
res = [sub for sub in test_list if all((ele % K == 0 for ele in sub))]
print('K Multiple elements tuples : ' + str(res))