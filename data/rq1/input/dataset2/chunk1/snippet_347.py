#Source: https://stackoverflow.com/questions/21622193/python-3-2-coroutine-attributeerror-generator-object-has-no-attribute-next
#!/usr/bin/python3.2
import sys

def match_text(pattern):
    line = (yield)
    if pattern in line:
        print(line)

x = match_text('apple')
x.next()

for line in input('>>>> '):
    if x.send(line):
        print(line)

x.close()