#Source: https://stackoverflow.com/questions/56913538/typeerror-with-scipy-optimize-when-minimizing-cost-func
from scipy.optimize import minimize

def func(W):
    W = W.reshape(1,9) #(1,9)
    Y = df0.values.reshape(49,1) #(49,1)
    X = df1.values.reshape(49,1) #(49,9)
    Z = np.dot(X, W.T) #(49, 1)
    Z = np.abs(Z - Y) #(49, 1)
    Cost = np.sum(Z ,axis=0, keepdims=True)
    return Cost[0][0]  #float

W = np.array([2,3,4,5,6,7,8,9,10])
cons = ({'type': 'ineq', 'fun': W[1]-W[0]})

result = minimize(func, x0=W0, constraints=cons, method="SLSQP")