#Source: https://stackoverflow.com/questions/56812810/sympy-physics-units-substitution-gives-typeerror
parse_expr('N') is sympify('N') # -> True
sympify('N') is evalf.N # -> True