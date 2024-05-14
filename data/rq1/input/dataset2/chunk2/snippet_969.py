#Source: https://stackoverflow.com/questions/50432564/typeerror-unsupported-operand-types-for-range-and-int
x = range(120, 200)
if x % 7 == 0 and x % 5 == 0:
    print(x)