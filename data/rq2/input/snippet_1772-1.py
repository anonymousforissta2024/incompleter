test_str1 = 'e:e:k:s:g'
print('The original string 1 is : ' + str(test_str1))
print('The original string 2 is : ' + str(test_str2))
delim = ':'
res = sorted(test_str1.split(':')) == sorted(test_str2.split(':'))
print('Are strings similar : ' + str(res))