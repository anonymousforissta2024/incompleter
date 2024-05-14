#Source: https://stackoverflow.com/questions/41323659/typeerror-cannot-convert-the-series-to-type-float
import scipy.special as sps
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from scipy.stats import gamma
from math import exp
########################################

### DADOS


dados= [2.3572833,0.7383197,14.1423990,2.0310423,7.1052727,1.8851099,12.9464459,4.4056236,1.0471756,0.4672236]

temp = pd.DataFrame(dados)

##########################################

def fx(x, t):
    prod = 1.0
    for i in range(0, len(x)):
        prod *= ((t[0]/t[1])* exp(- (x[i]/t[1]) ) * exp(-t[0] * exp(-(x[i]/t[1]) ) ) )
        return prod

#########################

def L(x, t):
    n = len(x)
    return fx(x,t)


##########################################

###  MCMC

def mcmc(N=[], k={"t1": 1, "t2": 1}, x=[]):
    chute = {"t1": [1], "t2": [1]}
    M = chute
    hiper = {"t1": [0.1, 0.1], "t2": [0.1, 0.1]} 
    contador = {"t1": [], "t2": []} 

    thetas = M.keys()
    for i in range(N - 1):
        for j in thetas:

            if j == "t1": 

                M[j].append( np.random.gamma(shape = M[j][-1], scale = k[j]) )
                lista = [ [ M[l][-1] for l in thetas] , [ M[l][-1] if l!=j else M[l][-2] for l in thetas ] ]
                t1 =  gamma.pdf(M[j][-1], a = hiper[j][0], scale = hiper[j][1]) * L(x, lista[0]) * gamma.pdf(M[j][-2], a = M[j][-1], scale = k[j])
                t2 =  gamma.pdf(M[j][-2], a = hiper[j][0], scale = hiper[j][1]) * L(x, lista[1]) * gamma.pdf(M[j][-1], a = M[j][-2], scale = k[j])          

                teste = (t1/t2)


            else:

                M[j].append( np.random.gamma(shape = M[j][-1], scale = k[j]) )
                lista = [ [ M[l][-1] for l in thetas] , [ M[l][-1] if l!=j else M[l][-2] for l in thetas ] ]
                t1 =  gamma.pdf(M[j][-1], a = hiper[j][0], scale = hiper[j][1]) * L(x, lista[0]) * gamma.pdf(M[j][-2], a = M[j][-1], scale = k[j])
                t2 =  gamma.pdf(M[j][-2], a = hiper[j][0], scale = hiper[j][1]) * L(x, lista[1]) * gamma.pdf(M[j][-1], a = M[j][-2], scale = k[j])          

                teste = (t1/t2)

        if (min(1, teste) < np.random.uniform(low=0, high=1)) or (np.isinf(teste)) or (np.isnan(teste)):
            M[j][-1] = M[j][-2]
            contador[j].append(0)
        else:
            contador[j].append(1)

    M = pd.DataFrame.from_dict(M)
    contador = pd.DataFrame.from_dict(contador)
    cont = contador.apply(sum)
    print(cont)

    return (M)

N = int(input("Entre com o N: "))

MP = mcmc(N=N, x=temp)

print(MP)