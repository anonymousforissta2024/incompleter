import re

def check(str, pattern):
    if re.search(pattern, str):
        print('Valid String')
    else:
        print('Invalid String')
check('2134', pattern)
check('349', pattern)