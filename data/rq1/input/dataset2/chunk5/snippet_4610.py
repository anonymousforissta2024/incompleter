#Source: https://stackoverflow.com/questions/31600668/nameerror-line-is-not-defined
import random
lines = list()
random.shuffle(line)
for i, line in enumerate(open('Filename.txt')):
    if i >= 21 and i < 89:
       print (line, end='')