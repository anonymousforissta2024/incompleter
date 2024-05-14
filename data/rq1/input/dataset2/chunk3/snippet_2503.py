#Source: https://stackoverflow.com/questions/55318044/patching-an-object-in-a-factory-class-yields-typeerror-super-argument-1-must
from unittest.mock import patch

class B():
    pass

class A(B):
    pass


class AFactory:

    def create(self):
        a = A()
        super(A, a).__init__()

with patch('mymain.A'):
    AFactory().create()