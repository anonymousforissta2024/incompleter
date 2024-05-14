#Source: https://stackoverflow.com/questions/40025837/cant-use-sympy-parser-in-my-class-typeerror-module-object-is-not-callable
from sympy.parsing import sympy_parser
expr=1/2
r='3/2'
r=sympy_parser(r)