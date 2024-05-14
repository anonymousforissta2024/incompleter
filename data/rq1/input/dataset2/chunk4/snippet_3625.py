#Source: https://stackoverflow.com/questions/72214567/nameerror-name-not-defined-for-function-that-is-already-defined-above-the-line
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:13:50 2022

% Problema Balisticii cu rezistenta aerului, Miron Alexandra, 222
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math
#%%Ex 1- sol analitica - fara rezistenta aerului

def Problema_Balisticii(m,v0,theta0,g):
    #b
    tmax=2*v0*np.sin(theta0)/g
    xmax=v0**2*np.sin(2*theta0)/g
    print('Distanta strabatuta este', xmax, 'si timpul de zbor este ', tmax)
    t=np.linspace(0,tmax,1000)
    #discretizam intervalul de timp [0,tmax]
    #a
    x=v0*np.cos(theta0)*t
    y=v0*np.sin(theta0)*t- g*t**2/2
    #c ttmax=t tilda max
    ttmax=v0*np.sin(theta0)/g
    ymax=(v0*np.sin(theta0))**2/(2*g)
    print('Inaltimea maxima este', ymax, 'si se atinge la momentul de timp t=',ttmax)
    
    return t,x,y

#%% traiectorie-fara rezistenta aerului 
m=4
v0=10
g=9.81

t1,x1,y1=Problema_Balisticii(m,v0,np.pi/6,g)
t2,x2,y2=Problema_Balisticii(m,v0,np.pi/4,g)
t3,x3,y3=Problema_Balisticii(m,v0,np.pi/3,g)
t4,x4,y4=Problema_Balisticii(m,v0,np.pi/2.5,g)
t5,x5,y5=Problema_Balisticii(m,v0,np.pi/2,g)

plt.figure()
plt.plot(x1,y1, label='$\pi/6$')
plt.plot(x2,y2, label='$\pi/4$')
plt.plot(x3,y3, label='$\pi/3$')
plt.plot(x4,y4, label='$\pi/2.5$')
plt.plot(x5,y5, label='$\pi/2$')
plt.legend()
plt.title('Problema balisticii fara rezistenta aerului')

#%% animatie miscare
plt.figure()
plt.axis([0, np.max(x2)+0.1,-0.1,np.max(y3)+0.1])
for i in range (len(x1)):
    plt.plot(x1[i],y1[i],'bo')
    plt.plot(x2[i],y2[i],'r*')
    plt.plot(x3[i],y3[i],'gp')
    plt.pause(0.1)
    
#%%
#sol numerica-sist de e.d.o
def Balistica_Euler_explicit_sist_Fara_rez(m,v0,theta0,g,t0,tf,h):
    N=math.floor((tf-t0)/h)+1
    t=np.zeros(N)
    z1=np.zeros(N)
    z2=np.zeros(N)
    z3=np.zeros(N)
    z4=np.zeros(N)
    t[0]=t0
    z1[0]=0
    z2[0]=v0*np.cos(theta0)
    z3[0]=0
    z4[0]=v0*np.sin(theta0)
    for i in range(1,N):
        t[i]=t0+i*h
        z1[i]=z1[i-1]+h*z2[i-1]
        z2[i]=z2[i-1]+h*0
        z3[i]=z3[i-1]+h*z4[i-1]
        z4[i]=z4[i-1]+h*(-g)
    return t, z1,z2,z3,z4

#%%
#sol numerica-sist de e.d.o
def Balistica_Euler_explicit_sist_cu_rez(m,v0,theta0,g,t0,tf,h):
    N=math.floor((tf-t0)/h)+1
    k=int(input("Coeficientul de rezistenta al aerului este: "))
    if k <= 0:
        print("Coeficientul de rezistenta trebuie sa fie mai mare ca 0, reintroduceti")
        k=int(input("Coeficientul de rezistenta al aerului este: "))

        
    t=np.zeros(N)
    z1=np.zeros(N)
    z2=np.zeros(N)
    z3=np.zeros(N)
    z4=np.zeros(N)
    t[0]=t0
    z1[0]=0
    z2[0]=v0*np.cos(theta0)
    z3[0]=0
    z4[0]=v0*np.sin(theta0)
    for i in range(1,N):
        t[i]=t0+i*h
        z1[i]=z1[i-1]+h*z2[i-1]
        z2[i]=z2[i-1]+h*(0-g*k**2*z2[i-1])
        z3[i]=z3[i-1]+h*z4[i-1]
        z4[i]=z4[i-1]+h*(-g-g*k**2*z4[i-1])
    return t, z1,z2,z3,z4

t0=0
tf=5
h=0.002
theta0=np.pi/6
t,z1,z2,z3,z4=Balistica_Euler_explicit_sist_cu_rez(m,v0,theta0,g,t0,tf,h)
x=z1
y=z3

index=np.where(y<0)[0][0]
plt.figure()
plt.plot(x[:index],y[:index])

t,z1,z2,z3,z4=Balistica_Euler_explicit_sist_Fara_rez(m,v0,theta0,g,t0,tf,h)
x=z1
y=z3

index=np.where(y<0)[0][0]
plt.figure()
plt.plot(x[:index],y[:index])