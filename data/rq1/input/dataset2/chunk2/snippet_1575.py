#Source: https://stackoverflow.com/questions/74504499/typeerror-function-missing-1-required-positional-argument-y
from names import names

def greet(x,y):
    template = "Hi {}, Hi {} ".format(x,y)
    print(template)


greet(names())