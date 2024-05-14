test_str1 = 'geeksforgeeks'
print('The original string is : ' + test_str1)
res = all((ele in test_str1 for ele in test_str2))
print('Does string contains all the characters of other list? : ' + str(res))