#Source: https://stackoverflow.com/questions/53727834/scipy-minimization-typeerror-int-object-is-not-callable
import random
import numpy as np
from scipy.optimize import minimize

def objective (h, b, Ip, Im, NIt, s, Qt):
    return h*Ip+b*Im

def constraint1 (h, b, Ip, Im, NIt, s, Qt):
    return NIt-s

def constraint2 (h, b, Ip, Im, NIt, s, Qt):
    return Qt

def test(T, d, RT, LT, h, b, I0, s):
    i = 1
    It = [0] * T
    Qt = [0] * T
    NIt = [0] * T
    It[0] = I0 - d[0]
    Qt[0] = d[0]
    NIt[0] = I0
    while i < T:
        if (i - LT) >= 0:
            It[i] = It[i-1] - d[i] + Qt[i-LT]
        else:
            It[i] = It[i-1] - d[i]
        NIt[i] = NIt[i-1] - d[i-1] + Qt[i-1]
        if It[i-1] > 0:
            Ip = It[i-1]
            Im = 0
        if It[i-1] < 0:
            Ip = 0
            Im = It[i-1]
        if It[i-1] == 0:
            Ip = 0
            Im = 0

        x0 = [h, b, Ip, Im, NIt[i], s, Qt[i]]
        con1 = {'type': 'ineq', 'fun': constraint1(h, b, Ip, Im, NIt[i], s, 
Qt[i])}
        con2 = {'type': 'ineq', 'fun': constraint2(h, b, Ip, Im, NIt[i], s, 
Qt[i])}
        cons = [con1, con2]
        sol = minimize(objective, x0, constraints=cons)

        Qt[i] = sol.Qt
        i += 1
    return It, NIt, Qt

d = []
for j in range(30):
    d.append(random.randint(0, 2)) 

[It, NIt, Qt] = test(30, d, 1, 1, 1, 1, 1, 2)