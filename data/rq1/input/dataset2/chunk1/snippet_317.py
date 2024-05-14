#Source: https://stackoverflow.com/questions/57457958/fibonacci-memoization-cannot-understand-the-reason-for-typeerror
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
            return memo[x]
    return helper
def fib(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

fib = memoize(fib)

print(fib(10))