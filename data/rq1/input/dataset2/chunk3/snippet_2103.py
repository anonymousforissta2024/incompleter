#Source: https://stackoverflow.com/questions/60073168/nameerror-while-using-functools-partial-inside-a-loop
from functools import partial

def glob_func(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x

class MyClass:

    local_func = partial(glob_func, 3, 1, 4)

    my_list = [local_func(num)
        for num in (
            40,
            70,
            90
        )]