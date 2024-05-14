import re
print('The original string is : ' + test_str)
res = len(re.findall('\\d+', test_str))
print('Count of numerics in string : ' + str(res))