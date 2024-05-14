#Source: https://stackoverflow.com/questions/71437991/typeerror-unsupported-operand-types-for-str-and-str-in-robot-framework
a=5
b=6
def Addition(a,b):
    s=a+b
    c = 3
    d = 2
    Sub(c,d)
    print(s)
def Sub(c,d):
    e=c-d
    print(e)
Addition(a,b)