#Source: https://stackoverflow.com/questions/74287845/python-recursion-problem-typeerror-unsupported-operand-types-for-int-and
def sum1(n):
    if n==0:
        return 0
    n+sum1(n-1)



print(sum1(5))