#Source: https://stackoverflow.com/questions/67128403/sympy-attributeerror-multiply-polynomial-by-complex-constant
from sympy import *
from sympy.abc import x, y, z, w

p = Poly(1.0*x, x, domain='C')
p*I