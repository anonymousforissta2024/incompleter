#Source: https://stackoverflow.com/questions/74969388/typeerror-unsupported-operand-types-for-list-and-list
import numpy as np
from getdist import MCSamples
import os
import imageio
import getdist.plots as gplot
import matplotlib.pyplot as plt
#from scipy.misc import derivative, pade
#from imageio import derivative, pade
from scipy.misc import derivative
#from imageio import pade
from matplotlib import rc
plt.rcParams['text.usetex']=True
plt.rcParams.update({'font.size': 20})
dire=os.getcwd() # This will automatically set your current working directory
print(dire)
from scalar_all_eqn import *


#Ophi_i,  rd, li, mi, Orad_i, h=0.7, Ob0=0.045, ns=0.96, sigma_8=0.8
#Ophi,  rd, li, mi,  Orad_i, h, sigma8
#Ophi,     rd, li, mi,  Orad_i, h, 0.045, 0.96, sigma8


samps=np.loadtxt("bao+masers+cmb+hz_c.dat")

names = ['Ophi','rd','li','mi','Orad_i','h','sigma8']
#names = ['Om0','rd','w0','wa','h','Or0','sigma8']

sample = MCSamples(samples=samps,names = names, labels = names)
#g = gplot.getSinglePlotter(chain_dir=r'%s'%dire)
#sample = g.sampleAnalyser.samplesForRoot('LCDM')
#sample = g.sampleAnalyser.samplesForRoot('7CPL')
param = sample.getParams()


mean=[]
lower=[]
upper=[]

lower1=[]
upper1=[]

lower2=[]
upper2=[]


def hubble_n_s(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 fun = scalarpow(Ophi,  rd, li, mi,  Orad_i, h, sigma8).hubble_normalized_z(z)
# H1 = 1 + q0
 return fun**2.

 
def hubble_norm_z(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 fun = scalarpow(Ophi,     rd, li, mi,  Orad_i*1e-5, h, 0.045, 0.96, sigma8).hubble_normalized_z(z)
 return fun 


def hubble_z(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 fun = scalarpow(Ophi,     rd, li, mi,  Orad_i*1e-5, h, 0.045, 0.96, sigma8).hubble_normalized_z(z)
# return fun*100.*h0
 return fun*100.*h
print(hubble_z(1.99,147.49,0.50,0.0032,0.11,0.7,0.8,0.0))


def equation_of_state_z(Ophi,  rd, li, mi,  Orad_i, h, sigma8,z):
 fun = scalarpow(Ophi,     rd, li, mi,  Orad_i*1e-5, h, 0.045, 0.96, sigma8).equation_of_state_z(z)
 return fun 
print(equation_of_state_z(1.99,147.49,0.50,0.0032,0.11,0.7,0.8,0.0))
 
 
z=np.linspace(0,1.5,10)
for i in z:


#z=np.linspace(0,5,10)
#for i in z:

  
  
  
  EoS = np.vectorize(equation_of_state_z) 
  derived = EoS(param.Ophi, param.rd, param.li, param.mi, param.Orad_i, param.h, param.sigma8,i)
   
# cpl OM(z) 
#  hubble_d = np.vectorize(dummy) 
#  hubble = np.vectorize(hubble_n_s)
#  derived = ((2.*(1.+i)*hubble_d(param.Ophi, param.rd, param.li, param.mi, param.Orad_i, param.h, param.sigma8,i))/3. -1.)/(1.- ((1.-param.Ophi-param.Orad_i)*(1.+i)**3./(hubble(param.Ophi, param.rd, param.li, param.mi, param.Orad_i, param.h, param.sigma8,i))))
  
  #m=sample.mean(derived)
  
  m=sample[~np.isnan(derived)].mean()
  #print(m)  


  print(np.nanmean(m))
    
  mean.append(m)
  
  #mean=mean+m  
  
  print(mean)

  #lcdm = np.sqrt(hubble_n_s(.27,4.68*1e-5,-1,0,z))
  s=sample.twoTailLimits(derived,0.683)
  s1=sample.twoTailLimits(derived,0.954)
  s2=sample.twoTailLimits(derived,0.997)
  lower.append(s[0])
  upper.append(s[1])
  lower1.append(s1[0])
  upper1.append(s1[1])
  lower2.append(s2[0])
  upper2.append(s2[1])
  print('z:%f mean:%f  lower:%f  upper:%f'%(i,m,s[0],s[1]))


  #s=sample.twoTailLimits(derived,0.683)
  #s1=sample.twoTailLimits(derived,0.954)
  #s2=sample.twoTailLimits(derived,0.997)
  #lower=lower+s[0]
  #upper=upper+s[1]
  #lower1=lower1+s1[0]
  #upper1=upper1+s1[1]
  #lower2=lower2+s2[0]
  #upper2=upper2+s2[1]
  #print('z:%f mean:%f  lower:%f  upper:%f'%(i,m,s[0],s[1]))

#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#rc('text', usetex=True)

#plt.plot((0, 2), (-1, -1) , 'k--',linewidth=0.4)

#plt.plot(z, mean, 'red', linewidth=.6)
plt.plot(z, (upper-lower)/2.0, 'blue', linewidth=.6)

#plt.plot(z,lcdm, 'k-',linewidth=0.3 )



plt.plot(z,lower,  'blueviolet',linewidth=.3)
plt.plot(z,upper,  'blueviolet',linewidth=.3)
plt.plot(z,lower1, 'darkviolet',linewidth=.3)
plt.plot(z,upper1, 'darkviolet',linewidth=.3)
plt.fill_between(z,lower,upper, color='mediumorchid', alpha=0.5)
plt.fill_between(z,lower1,upper1, color='violet', alpha=0.5)
#plt.plot(z,lower2, 'r-.',linewidth=1.5)
#plt.plot(z,upper2, 'r-.',linewidth=1.5)
#plt.xlim(0.001,1.3)
#plt.plot(z,(upper-lower)/2.0, 'blueviolet',linewidth=.3)


plt.xlim(0,1.5)
plt.ylim(-1.5,-0.7)

plt.xlabel(r'$z$')
plt.ylabel(r'$w_{DE}(z)$')
plt.savefig('w_mean.pdf',bbox_inches='tight')