print('The original list is : ' + str(test_list))
res = ''.join((ele for sub in test_list for ele in sub))
print('The String after join : ' + res)