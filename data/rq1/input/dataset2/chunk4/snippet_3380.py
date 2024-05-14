#Source: https://stackoverflow.com/questions/64683421/how-to-adjust-a-dict-of-one-class-so-it-works-in-another-when-using-type
class A(object):
    def __init__(self):
        print('A', self.__dict__)


class B(object):
    def __init__(self):
        print('B', self.__dict__)

F = type('C', (B,), A.__dict__.copy())
F()