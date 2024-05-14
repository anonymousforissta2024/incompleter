#Source: https://stackoverflow.com/questions/59908880/jacobian-matrix-typeerror-function-object-does-not-support-item-assignment
import autograd.numpy as np
from autograd import grad, jacobian

def f(x):
    f = np.zeros(len(x))
    f[0] = np.sin(x[0])+x[1]**2 +np.log(x[2])-7 
    f[1] = 3.0*x[0] + 2.0**x[1] - x[2]**3 + 1.0
    f[2] = x[0] + x[1] + x[2] - 5.0
    return f
x = np.array([-1.0,0.2,0.3])
gradient_cost = grad(f)
jacobian_cost = jacobian(f)

gradient_cost(x)
jacobian_cost(np.array([x,x,x]))