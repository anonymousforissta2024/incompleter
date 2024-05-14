#Source: https://stackoverflow.com/questions/66885501/why-do-i-recieve-typeerror-module-object-is-not-callable-for-scipy-integrat
import math 
import scipy.integrate._quadrature as quad         

def func(x):
    return x*np.sin(x)

def exactIntegral(a, b):
    Iab = -b*np.cos(b) + np.sin(b) + a*np.cos(b) - np.sin(a)
    return Iab

a = 0.0
b = 2.0 

exact = exactIntegral(a, b)
estimate = quad(func, a, b)                               #TypeError: 'module' object is not callable

print('Exact %1.6f Numerical %1.6f' %(exact, estimate[0]))
print('Error %1.3e' % np.abs(exact-estimate[0]))