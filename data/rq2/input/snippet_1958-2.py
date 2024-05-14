test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78,)]
print('The original list is : ' + str(test_list))
res = [sub for sub in test_list if all((len(str(ele)) == K for ele in sub))]
print('The Extracted tuples : ' + str(res))