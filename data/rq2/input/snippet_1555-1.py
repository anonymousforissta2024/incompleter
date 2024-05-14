import re

def CntSubstr(pattern, string):
    a = [m.start() for m in re.finditer(pattern, string)]
    return a
string = 'geeksforgeeksforgeeks'
print(CntSubstr(pattern, string))