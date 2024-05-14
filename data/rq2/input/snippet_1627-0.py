print('The original list is : ' + str(test_list))
res = [sub for sub in test_list if not all((ele == None for ele in sub))]
print('Removed None Tuples : ' + str(res))