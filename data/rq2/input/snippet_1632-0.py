print('The original list is : ' + str(test_list))
res = [sub for sub in test_list if all((ele >= 0 for ele in sub))]
print('Positive elements Tuples : ' + str(res))