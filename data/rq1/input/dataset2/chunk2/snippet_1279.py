#Source: https://stackoverflow.com/questions/61432536/nameerror-name-pi-is-not-defined
import math
from math import pi,cos,sin,tan,atan

# eval('a + sin(p/2)', bindings)    # 'sin' not defined

def Formula(expression):
    class F:

        def __init__(self,kwargs):
            s = kwargs.replace(',','')
            l=((s.replace('=',' ').split()))

            it = iter(l)

            self.res_dct = dict(zip(it,it))
            self.res_dct=  {k:float(v) for k, v in self.res_dct.items()}

            class Foo:
                def setAllWithKwArgs(self, **kwargs):
                    for key, value in kwargs.items():
                        setattr(self, key, value)

        def calc(self):

            return eval(expression,self.res_dct)

    return F

triangle_hypotenuse = Formula('(a*a + b*b)**0.5')
print(triangle_hypotenuse('a=3, b=4') .calc())

cylinder_volume = Formula('PI * r**2 * h')
cylinder_volume('r= 1, h=2') .calc()