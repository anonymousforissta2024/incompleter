#Source: https://stackoverflow.com/questions/73452966/python-error-typeerror-float-argument-must-be-a-string-or-a-real-number-not
import re
name = input('Enter File: ')
if len(name) < 1 :
    name = 'sample.txt'
handle = open(name)
numlist = list()
for line in handle :
    line = line.rstrip()
    items = re.findall('[0-9]+', line)
    if len(items) > 0 :
        #print(items)
        num = float(items[0: ])
        numlist.append(num)
print(sum(numlist))