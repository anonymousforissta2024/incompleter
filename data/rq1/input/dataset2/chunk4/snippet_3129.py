#Source: https://stackoverflow.com/questions/72094887/int-object-is-not-iterable-typeerror
n=100
from collections import OrderedDict

for i in range (-n, n):
  if (i % 3 == 0) or (i % 5 == 0):
    print(i)
  elif (i % 3 == 0) and (i % 5 ==0):
    print(i)
  elif i < 0:
    pass
sum(i)