#Source: https://stackoverflow.com/questions/33423431/python-3-5-0-typeerror-cant-multiply-sequence-by-non-int-of-type-float
import random

f= open('file.txt','r')
namesList = []

for line in f:
    namesList.append(line.strip())

print('There are %d names in list and we will choose %.0f from the list.' % (len(namesList), float(len(namesList))*0.25))

print('Names choosed was %s' % (random.sample(namesList, len(namesList)*0.25)))

f.close()