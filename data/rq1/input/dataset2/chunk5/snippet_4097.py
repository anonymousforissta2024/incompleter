#Source: https://stackoverflow.com/questions/44857367/in-python-3-x-typeerror-unsupported-operand-types-for-complex-and-comp
class Test():
    def __init__(self):
        self._x=(1,2)
    def __div__(self,div_fraction):
        return (self._x[0]*div_fraction[1],self._x[1]*div_fraction[0])

y=Test()
z=y/(1,3)
print(z)