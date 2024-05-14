#Source: https://stackoverflow.com/questions/53916900/sympy-returns-typeerror-when-putting-irrational-in-a-fraction
import sympy
sympy.init_printing(use_unicode=True)

sympy.Rational(3, sympy.sqrt(3))