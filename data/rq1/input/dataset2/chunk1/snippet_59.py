#Source: https://stackoverflow.com/questions/39753260/sympy-to-numpy-causes-the-attributeerror-symbol-object-has-no-attribute-cos
import sympy as sp
import numpy as np
from sympy import init_printing
init_printing()
t_1,t_2,X_1,X_2,Y_1,Y_2,X_c1,X_c2,Y_c1,Y_c2,a_1,a_2,psi_1,psi_2,b_1,b_2= sp.symbols('t_1 t_2 X_1 X_2 Y_1 Y_2 X_c1 X_c2 Y_c1 Y_c2 a_1 a_2 psi_1 psi_2 b_1 b_2')

X_1=X_c1 + (a_1 * sp.cos(t_1) * sp.cos(psi_1)) - ((b_1) * sp.sin(t_1)* sp.sin(psi_1))

X_2=X_c2 + (a_2 * sp.cos(t_2) * sp.cos(psi_2)) - ((b_2) * sp.sin(t_2)* sp.sin(psi_2))

Y_1=Y_c1 + (a_1 * sp.cos(t_1) * sp.sin(psi_1)) + ((b_1) * sp.sin(t_1)* sp.cos(psi_1))

Y_2=Y_c2 + (a_2 * sp.cos(t_2) * sp.sin(psi_2)) + ((b_2) * sp.sin(t_2)* sp.sin(psi_2))

D=(((X_2-X_1)**2) + ((Y_2-Y_1)**2))**0.5

y_1=sp.diff(D,t_1)

y_2=sp.diff(D,t_2)

f=sp.lambdify(t_1, y_1, "numpy")

g=sp.lambdify(t_2, y_2, "numpy")