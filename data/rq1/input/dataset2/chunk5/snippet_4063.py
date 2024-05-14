#Source: https://stackoverflow.com/questions/57941113/typeerror-numpy-ndarray-with-scipy-optimize-minimize-numpy-ndarray-object-is
constraints = [
    {'type' : 'ineq', 'fun' : AA},
    {'type' : 'ineq', 'fun' : Ev},
    {'type' : 'eq', 'fun' : Aeq},
    {'type' : 'eq', 'fun' : Beq}
]
bnds = ((-5, 5))

z = minimize(lambda z: cost(z,to), x0=z0, constraints=constraints, method='SLSQP')