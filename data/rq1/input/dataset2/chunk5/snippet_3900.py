#Source: https://stackoverflow.com/questions/54452804/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-solution
import math as m
import pylab as pyl
import numpy as np

#normal distribution function
def normal(x,mu,sigma):
    P=(1/(m.sqrt(2*m.pi*sigma**2)))*(m.exp((-(x-mu)**2)/2*sigma**2))
    return P

#solution
x = np.linspace(-5,5,1000)
P = normal(x,0,1)
#plotting the function
pyl.plot(x,P)
pyl.show()