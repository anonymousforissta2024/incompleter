#Source: https://stackoverflow.com/questions/50553835/attributeerror-occurs-in-datetime-expression
from datetime import datetime

s = 'Hello, Pythoneers'
print(s == eval(repr(s)))  # no errors here

today = datetime.now()
print(today == eval(repr(today))) # error occurs here