#Source: https://stackoverflow.com/questions/61851719/unsupported-operand-type-error-while-evaluating-gradient-using-sympy
import matplotlib.pyplot as plt 
import numpy as np
import math
import sympy as sym

x,y = sym.symbols('x y')

 #objective function
def objective(p): 
    x = p[0]
    y = p[1]
    return -(y+47)*sym.sin(sym.sqrt(abs((x/2)+y+47))) - x*sym.sin(sym.sqrt(abs(x-(y+47))))

 #gradient wrt x
def gradient_1(p): 
    g0 = sym.diff(objective([x,y]),x)
    return g0.subs(x,p[0]).subs(y,p[1])

#gradient wrt y
def gradient_2(p):
    g1 = sym.diff(objective([x,y]),y)
    return g1.subs(x,p[0]).subs(y,p[1])

#initial guess
x = [-450,-450]

#learning rate
alpha = 0.135

#initialization
iter = 0
e = 1000
grad = np.array([])
error = np.array([])

#gradient descent 
while e > 0.000000001:
    t = objective(x)
    grad = [gradient_1(x),gradient_2(x)]
    change = np.dot(-alpha,grad)
    x = np.add(x,change)
    e = abs(objective(x)-t)
    error = np.append(error,e)
    iter = iter+1
    print("ITERATION NUMBER = ",iter)

#printing optimized values
print(x)
#plotting error v/s iteration
i = np.arange(1,iter+1)    
plt.plot(i,error)
plt.xlabel("Iterations")
plt.ylabel("Error") 