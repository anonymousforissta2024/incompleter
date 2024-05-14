#Source: https://stackoverflow.com/questions/48026466/typeerror-unsupported-operand-types-for-int-and-nonetype-while-adding
import cv2
import numpy as np

img1=cv2.imread('3.jpg')
img2=cv2.imread('4.jpg')

add = img1 + img2

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows