#Source: https://stackoverflow.com/questions/54619517/receiving-error-attributeerror-module-cv2-cv2-has-no-attribute-comparehist
import numpy as np
import cv2 as cv

img = cv.imread('../data/im3.jpg')
img2 = cv.imread('../data/im4.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()
kp, des1 = sift.detectAndCompute(gray,None)
kp2, des2 = sift.detectAndCompute(gray2,None)


print(cv.CompareHist(des1[0], des2[0], CV_COMP_CORREL))