#Source: https://stackoverflow.com/questions/54602828/typeerror-unsupported-operand-types-for-tuple-and-int-why-i-can-not-s
from numba import jit
import numpy as np
import time


@jit
def foo(x: int, y: int) ->float:
    tt = time.time()
    s = 0
    for i in range(x,y):
           s += i
    print("Time used: {} sec".format(time.time() - tt))
    return s


print("value of foo", foo(1, 1000))


def foo2(x, y)->float:
    tt = time.time()
    s = 0
    for i in range(x, y):
       s += i
    print("Time used for foo2: {} sec".format(time.time() - tt))
    return s


print("value of foo2", foo2(1, 1000))

a= foo(1, 1000)
b= foo2(1, 1000)
print (a-b)
print(type(a))
print(type(b))
print(type(foo2((1, 1000)-foo(1, 1000))))