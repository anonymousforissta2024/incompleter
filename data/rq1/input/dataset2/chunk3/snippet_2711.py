#Source: https://stackoverflow.com/questions/52671829/trying-to-split-a-string-but-i-keep-getting-this-error-type-error-must-be-str
from random import *
number = randint(1000,9999)
strnumber = str(number)
a,b,c,d = strnumber.split([strnumber[i:i+1] for i in range(0, len(strnumber), 1)])
print(a)
print(b)
print(c)
print(d)