#Source: https://stackoverflow.com/questions/13906623/using-pickle-dump-typeerror-must-be-str-not-bytes
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