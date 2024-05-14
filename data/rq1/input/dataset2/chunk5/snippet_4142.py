#Source: https://stackoverflow.com/questions/55817018/undefined-name-error-when-minimizing-using-scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from sklearn.metrics import r2_score

url = 'test_data.txt'
z = pd.read_csv(url)
#
e1 = z['strain'].values
sigx = z['stress'].values
e=np.array(e1)
sig1=np.array(sigx)
#print (sig1)

def sig2(e):
    j=[1000,0.2]
    return np.mean((sig1-(j[0]*np.power(e,j[1])))*(sig1-(j[0]*np.power(e,j[1]))))
print (sig2(e))

res= minimize(sig2,j)
print(res)