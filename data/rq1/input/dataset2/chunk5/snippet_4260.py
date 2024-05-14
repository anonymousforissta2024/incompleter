#Source: https://stackoverflow.com/questions/57422230/receiving-a-typeerror-when-using-scipy-integrate-quad-cant-convert-complex-to
def H(G):
    return integrate.quad(lambda x: (np.pi*(np.exp(-x)))/(1+1j*G),0,np.inf)
scipy.optimize.fsolve(lambda G: f(G),x0 = 1)