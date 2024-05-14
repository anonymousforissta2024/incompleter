import re
print('The original string is : ' + str(test_str))
res = re.split('a|e|i|o|u', test_str)
print('The splitted string : ' + str(res))