#Source: https://stackoverflow.com/questions/67987726/typeerror-minimize-got-multiple-values-for-argument-methodwithout-kwargs
from scipy.optimize import minimize
def fun1(x,Cnoi,M):
    return np.linalg.norm(Cnoi - np.matmul(M,x))**2

minimize(fun1, x0, Cnoi, M, method='SLSQP', bounds=bnds, constraints=cons)