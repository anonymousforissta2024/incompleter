#Source: https://stackoverflow.com/questions/55533645/nameerror-when-using-composite-pseudovoigt-model
from lmfit.models import LorentzianModel, PseudoVoigtModel
import numpy as np
import matplotlib.pyplot as plt

def make_model_L(num):
    pref = "f{0}_".format(num)
    model = LorentzianModel(prefix = pref)
    model.set_param_hint(pref+'amplitude', value=amplitude[num], min=0, max=5*amplitude[num])
    model.set_param_hint(pref+'center', value=center[num], min=center[num]-0.5, max=center[num]+0.5)
    model.set_param_hint(pref+'sigma', value=width[num], min=0, max=2)
    return model


def make_model_V(num):
    pref = "f{0}_".format(num)
    model = PseudoVoigtModel(prefix = pref)
    print('before',model.param_names)
    model.set_param_hint(pref+'fraction',value = 0.7, vary = False)
    model.set_param_hint(pref+'amplitude', value=amplitude[num], min=0, max=5*amplitude[num])
    model.set_param_hint(pref+'center', value=center[num], min=center[num]-0.5, max=center[num]+0.5)
    model.set_param_hint(pref+'fwhm', value=3, min=3/5, max=3*5)
    model.set_param_hint(pref+'sigma', value=1, min=0, max=2)
    model.set_param_hint(pref+'height', value=1, min=-np.inf, max=np.inf, expr='(((1-fraction)*amplitude)/(sigma*sqrt(pi/log(2)))+(fraction*amplitude)/(pi*sigma))')
    print(model.param_names)
    return model

# Some really coarse "data"
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
y = [1,1,1,1,3,4,5,6,5,4,3,1,1,1,1,1,1,1,1,3,4,5,6,5,4,3,1,1,1,1]

peaks_in_interval = np.array([43, 159, 191, 296, 435, 544])
amplitude = [3,3]
width = [1,1]
center = [7,21]

mod = None
for i in range(len(center)):
    #this_mod = make_model_L(i)
    this_mod = make_model_V(i)
    if mod is None:
        mod = this_mod
    else:
        mod = mod + this_mod

out=mod.fit(y, x=x, method='leastsq')
plt.interactive(True)
print(out.fit_report())
plt.plot(x, y)
plt.plot(x, out.best_fit, label='best fit')
plt.plot(x, out.init_fit, 'r--', label='fit with initial values')
plt.show()