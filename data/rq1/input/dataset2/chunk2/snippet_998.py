#Source: https://stackoverflow.com/questions/56812810/sympy-physics-units-substitution-gives-typeerror
from sympy.parsing.sympy_parser import parse_expr
from sympy.physics import units

type(units.newton) # -> sympy.physics.units.quantities.Quantity

parse_expr('2*Newton').subs({'Newton':units.newton}) # -> 2N
parse_expr('2*newton').subs({'newton':units.newton}) # -> 2N
parse_expr('2*n').subs({'n':units.newton}) # -> 2N
parse_expr('2*N').subs({'N':units.newton}) # -> raises TypeError below
parse_expr('N').subs() # -> raises AttributeError below
parse_expr('N') # -> <function sympy.core.evalf.N(x, n=15, **options)>