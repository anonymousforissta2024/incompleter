#Source: https://stackoverflow.com/questions/58987855/im-seeing-typeerror-tuple-object-does-not-support-item-assignment-on-spyde
#import libraries
import numpy as np
import matplotlib.pyplot as plt

def dydt(t,y):
    dfdt = y / ((t + 1) ** 2)
    return dfdt

def IVPsolver2(dydt_fun, y0, t0, t1, t2, tf, h):
    n = 50 #points
    h = (tf-t0)/(n-1) #step size
    t = np.linspace(t0,t1,t2,tf,n)
    y = np.zeros(n) #preallocate zeros
    yp = np.zeros(n)
    m = np.zeros(n)
    mc = np.zeros(n)
    yp[0] = y0 #first yp at y0
    y[0] = y0 #y is 0
    t[0] = 0 #t is 0
    for i in range(0,n-1):
        m[i] = dydt_fun(t[i-1],y[i-1]) #calculating slope
        yp[i] = y[i] + m[i]*h #calculating predicted y at slope y
        mc[i] = dydt_fun(t[i+1],yp[i]) #slope corrector, 2 step
        t[i+1] = t[i] + h #t going by stepsize
        y[i+1] = y[i] + ((m[i]+mc[i])/2)*h #corrected y
    return t, y

def main(): #plotting  
    x2, y2 = IVPsolver2(dydt, 1, 0, 0.2, 0.4, 0.6, 0.2)
    plt.plot(x2,y2, 'o', mfc = 'purple')

    return
main()