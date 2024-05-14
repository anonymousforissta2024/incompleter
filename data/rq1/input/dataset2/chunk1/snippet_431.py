#Source: https://stackoverflow.com/questions/61088264/getting-a-typeerror-numpy-float64-object-is-not-callable-error-in-program
import numpy as np

#Defining how to integrate a function using the trapezium rule
def integrate(f, a, b, N:int):
    h = (b-a) / N       
    s = 0               

    for i in range(1,N):        
        c = f(a + i*h)
        s = s + c

    Area = h*(0.5*f(a) + 0.5*f(b) + s)
    return Area

def func(o, m, x):
    return np.cos(m*o - x*np.sin(o))        #1st attempt at defining the bessel function

def J(m,x):     
    return (1 / np.pi) * integrate(func(0, m, x), 0, np.pi, 10000)

#Produce range of x-values from 0 to 20.
xvals = np.linspace(0,20,200)

#Calculating the value of the bessel function for each value of x and m
for i in range(200):

    for j in range(3):
        bessel = J(j, xvals[i])
        print("x: {}, m: {}, Val: {}".format(xvals[i], j, bessel))      #Print statement to check the program is functioning correctly before moving on to the next stage