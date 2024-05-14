#Source: https://stackoverflow.com/questions/69817812/python-pickle-throws-typeerror
import os
import pickle
from pickle import *
os.chdir('c:/Python26/progfiles/')

def storvars(vdict):      
    f = open('varstor.txt','w')
    pickle.dump(vdict,f,)
    f.close()
    return

mydict = {'name':'john','gender':'male','age':'45'}
storvars(mydict)