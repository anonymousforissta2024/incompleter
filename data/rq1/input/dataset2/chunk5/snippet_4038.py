#Source: https://stackoverflow.com/questions/59286117/google-colab-attributeerror-numpy-ndarray-object-has-no-attribute-seek-an
import matplotlib.pyplot as plt
import numpy as np
import sys
import PIL
import cv2

rgb = cv2.imread("/content/teste/LC08_L1TP_222063_20180702_20180716_01_T1_1_3.tif")
tir = cv2.imread("/content/teste/LC08_L1TP_222063_20180702_20180716_01_T1_TIR_1_3.tif")
qb = cv2.imread("/content/teste/LC08_L1TP_222063_20180702_20180716_01_T1_QB_1_3.tif")


list_im = [rgb, tir, qb]
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Trifecta.jpg' )