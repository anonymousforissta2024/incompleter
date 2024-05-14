import itertools
n = 10

def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = (y, x + y)
print('First 10 Fibonacci numbers:')
print(result)
square = lambda x: x * x
print('\nAfter squaring said numbers of the list:')
print(list(map(square, result)))