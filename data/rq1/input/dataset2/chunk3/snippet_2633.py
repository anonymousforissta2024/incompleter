#Source: https://stackoverflow.com/questions/50616850/python-3-sympy-typeerror-cant-convert-expression-to-float
import math
from sympy import solve, Poly, Eq, Function, exp
from sympy.abc import x, y, z, a, b, c
print (solve((((math.sin((((x - (a + 1)) / (b - a)) - 0.5) * math.pi) + 1) / 2) * 1) / math.pow(1.00571, (b + 1 - x)) *c,  a, b,c))