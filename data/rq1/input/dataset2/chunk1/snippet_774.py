#Source: https://stackoverflow.com/questions/42573566/python-decorator-typeerror-function-takes-1-positional-argument-but-2-were-giv
@log_calls
def fizz_buzz_or_number(i):
    ''' Return "fizz" if i is divisible by 3, "buzz" if by
        5, and "fizzbuzz" if both; otherwise, return i. '''
    if i % 15 == 0:
        return 'fizzbuzz'
    elif i % 3 == 0:
        return 'fizz'
    elif i % 5 == 0:
        return 'buzz'
    else:
        return i