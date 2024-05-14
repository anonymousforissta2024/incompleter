#Source: https://stackoverflow.com/questions/59459414/sympy-typeerror-cant-convert-expression-to-float
import sympy as sp
from scipy.integrate import quad
import math
def f(x):
    return math.exp(-2.0*math.pi*sp.I*x*n)
x = sp.Symbol('x')
n = sp.Symbol('n')
res,err = quad(f,0,1)
print(res)