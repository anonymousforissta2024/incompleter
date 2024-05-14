import re

def CntSubstr(pattern, string):
    a = [m.start() for m in re.finditer(pattern, string)]
    return a
pattern = 'geeksforgeeks'
print(CntSubstr(pattern, string))