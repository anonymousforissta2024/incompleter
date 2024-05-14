print('The original list is : ' + str(test_list))
cus_eles = [6, 7, 8]
res = [[sub + (cus_eles[idx],) for sub in val] for idx, val in enumerate(test_list)]
print('The matrix after row elements addition : ' + str(res))