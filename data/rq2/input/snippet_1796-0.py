import re
test_str = 'geeksgeeks are geeks for all geeksgeeksgeeks'
print('The original string is : ' + str(test_str))
res = max(re.findall('((?:' + re.escape(sub_str) + ')*)', test_str), key=len)
print('The maximum run of Substring : ' + res)