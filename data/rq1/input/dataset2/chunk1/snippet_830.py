#Source: https://stackoverflow.com/questions/3969726/attributeerror-module-object-has-no-attribute-urlopen
import urllib

file = urllib.urlopen("http://www.python.org")
s = file.read()
f.close()

#I'm guessing this would output the html source code?
print(s)