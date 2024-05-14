#Source: https://stackoverflow.com/questions/69520437/typeerror-float-object-is-not-subscriptable-when-accessing-the-float-elements
import numpy as np
from math import sqrt
import itertools

class MyClass():
    id = itertools.count(start=1)

    def __init__(self, location = None):
        self.id = next(MyClass.id)
        self.location = np.random.uniform(0, 1, size=(1, 2)).tolist()[0]


    def __iter__(self):
        for _ in self.__dict__.values():
            yield _

    def f(self, obj):
        return sqrt((self.location[0][0] - obj.location[0][0]) ** 2 + (self.location[0][1] - obj.location[0][1]) ** 2)

    def g(self, objs):
        flag = True
        for obj in objs:
            if self.f(obj) > 0.8:
                flag = False
                break
        return flag

def do():
    objs = []
    first_obj = MyClass()
    objs.append(first_obj)
    counter = 1
    while counter != 10:
        next_obj = MyClass()
        if next_obj.g(objs):
            objs.append(next_obj)
            counter = counter + 1
    return objs

objs = do()