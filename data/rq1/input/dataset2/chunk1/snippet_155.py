#Source: https://stackoverflow.com/questions/50716931/unittest-mock-and-multiple-inheritance-typeerror-metaclass-conflict
from class_a import A

class B:
    pass

class C(A, B):
    pass