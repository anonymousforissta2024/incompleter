#Source: https://stackoverflow.com/questions/40317307/python-typeerror-unsupported-operand-types-for-int-and-nonetype
from functools import reduce
def char2num(s1):
    if s1 == '.':
        pass
    else:
        return  {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s1]

def str2float(s):
    count = 0

    ans = reduce(lambda x, y: 10*x + y,map(char2num,s))

    for x in range(len(s)):
        if s[x] == '.':
            count = x
            break
        else:
            pass
    for n in range(count):
        ans /= 10
    return ans
print('str2float(\'123.456\') =', str2float('123.456'))