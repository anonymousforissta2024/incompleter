#Source: https://stackoverflow.com/questions/61370217/sympy-bisection-method-typeerror-cannot-determine-truth-value-of-relational
from sympy import plot_implicit, latex, lambdify, Float
from sympy.abc import x
from sympy.parsing.latex import parse_latex

eq = input("Latex equation: ")    
raw_equation = eq.replace("=0", "").replace("= 0", "").replace("e", "E")
equation = parse_latex("y = " + raw_equation)
f = lambdify(x, parse_latex(self.__raw_equation), 'numpy')

# Bisection
a = 0 # start interval
b = 1 # end interval

eps = a - b
r = None
nlimit = 8
for n in range(nlimit):
    c = (a + b) / 2
    fd = {a: f(a), b: f(b), c: f(c)}
    solved = False
    for v in [a, b, c]:
        if fd[v] == 0:
            r = "Iterations: {} - Result: {}".format(n + 1, v)
            solved = True
            break
    if solved:
        break
    if fd[a]*fd[c] > 0:  # Opposite sign a and c <-- ERROR
        b = c
    else:  # Opposite sign b and c
        a = c
...