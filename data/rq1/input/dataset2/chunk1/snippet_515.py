#Source: https://stackoverflow.com/questions/46823004/sympy-typeerror-cannot-determine-truth-value-of-relational-when-using-sympy
x = symbols('x',real=True)
h = symbols('h',real=True)
f = symbols('f',cls=Function)    
sym_dexpr = f_diff.subs(f(x), x*exp(-x**2)).doit()
f_diff = f(x).diff(x,1)
expr_diff = as_finite_diff(f_diff, [x, x-h,x-2*h,x-3*h])
w=Wild('w')
c=Wild('c')
patterns = [arg.match(c*f(w)) for arg in expr_diff.args]
coefficients = [t[c] for t in sorted(patterns, key=lambda t:t[w])]
print(coefficients)