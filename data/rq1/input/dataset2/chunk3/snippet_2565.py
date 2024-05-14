#Source: https://stackoverflow.com/questions/60322770/typeerror-with-validation-decorator-in-class-method
import numpy as np

def validate_decorator(func):
    def func_wrapper(value):
        if value < 0:
            raise Exception("Not valid!")
        return func(value)
    return func_wrapper


class MyClass:
    def __init__(self):
        self.my_array = np.zeros(shape=(10,))
        self.idx = 0

    @validate_decorator
    def insert_value(self, value):
        self.my_array[self.idx] = value
        self.idx += 1

    def __str__(self):
        return f"{self.my_array[:self.idx]}"


a = MyClass()
a.insert_value(3.14)