#Source: https://stackoverflow.com/questions/52726959/i-have-a-problem-with-this-error-message-typeerror-unsupported-operand-types
import csv
import random
import math
import operator

with open('iris.csv', 'r') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))