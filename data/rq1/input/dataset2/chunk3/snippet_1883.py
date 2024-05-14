#Source: https://stackoverflow.com/questions/56731528/python-threading-typeerror-testmethod-takes-2-positional-arguments-but-12-w
from threading import Thread

class TestClass:
    def _testmethod(self, argument):
        print(argument)

    def __init__(self, arg):
        self.T = Thread(target=self._testmethod, args=(arg,))
        self.T.start()        

C = TestClass("hello world")