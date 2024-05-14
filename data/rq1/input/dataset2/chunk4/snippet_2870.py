#Source: https://stackoverflow.com/questions/71296396/why-is-this-showing-type-error-in-python
import math
import os
import random
import re
import sys



def timeConversion(s):
    if "P" in s:
        x = re.split("\W", s)
        y = int(x[0]) + 12
        z = str(y)
        a = re.sub("^\d\d", z, s)
        b = re.sub("[a-zA-Z]", "", a)
        print(b)
    else:
        b = re.sub("[a-zA-z]", "", s)
        print(b)

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    fptr.write(result, + '\n')

    fptr.close()