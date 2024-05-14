#Source: https://stackoverflow.com/questions/50382699/typeerror-while-using-scipy-optimization-algorithms-with-rbf-kernel-in-gaussianp
import numpy as np
from scipy.optimize import minimize,least_squares
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from scipy.optimize import least_squares,rosen

def trust_region_optimizer(obj_func, initial_theta, bounds):
    trust_region_method = least_squares(1/obj_func,initial_theta,bounds,method='trf')
    return (trust_region_method.x,trust_region_method.fun)

X=np.random.random((10,4))
y=np.random.random((10,1))
kernel = C(1.0, (1e-5, 1e5)) * RBF(10.0)
gp = GaussianProcessRegressor(kernel=kernel, optimizer = trust_region_optimizer(rosen,[10,20,30,40], [0,100]), alpha =1.2, n_restarts_optimizer=10)
gp.fit(X, y)