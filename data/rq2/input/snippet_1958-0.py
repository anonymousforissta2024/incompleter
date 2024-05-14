print('The original list is : ' + str(test_list))
K = 2
res = [sub for sub in test_list if all((len(str(ele)) == K for ele in sub))]
print('The Extracted tuples : ' + str(res))