#Source: https://stackoverflow.com/questions/49833108/python-attribute-error-after-result-is-outputed
import re

pattern = re.compile(r'(?<=\>)(.*?)(?=\|)')

# open input file
input_file = open('input.fas', 'r')

while True:
    line = input_file.readline()
    if line == '' or line is None:
        print('EOF')
        break
    else:
        output = pattern.search(line).group()
        print(output)