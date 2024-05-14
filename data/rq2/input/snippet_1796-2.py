import re
print('The original string is : ' + str(test_str))
sub_str = 'geeks'
res = max(re.findall('((?:' + re.escape(sub_str) + ')*)', test_str), key=len)
print('The maximum run of Substring : ' + res)