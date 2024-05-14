#Source: https://stackoverflow.com/questions/47418938/typeerror-unsupported-operand-types-for-int-and-tuple
#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
import random as r
from math import *



def ouvrir(nomimage):
    img=Image.open(nomimage)  
    return img

def affiche(img):
    img.show()


def imc2img(imc,n):
    img=Image.new("F",imc.size) 
    pixc=imc.load() 
    pixg=img.load()
    width = imc.size[0] 
    height=imc.size[1]
    for j in range(height):
        for i in range(width):
            pixg[i,j]=pixc[i,j][n]
    return img

def imc2r(ims):
    imr=imc2img(ims,1)
    return imr

def inverse_image(ims):
    img=Image.new("L",ims.size)
    pixc=ims.load()
    pixg=img.load()
    width=ims.size[0]
    height=ims.size[1]
    for j in range(height):
        for i in range(width):
            imi=pixg[i,j]=pixc[(255-i),(255-j)]
    return imi