#Source: https://stackoverflow.com/questions/64962517/typeerror-expected-str-bytes-or-os-pathlike-object-not-numpy-ndarray
from PIL import Image

import numpy as np

from lsd import *

import cv2

im = cv2.imread('/home/lenovo/Downloads/python-lsd-master/test_data/chairs.pgm')

#fullName = '1.jpg'

folder, imgName = os.path.split(im)

src = cv2.imread(im, cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

lines =lsd.__module__

#path1=os.path.normpath('/home/lenovo/pylsd/example/751626ntl.txt')

for i in range(lines.shape[0]):

    pt1 = (int(lines[i, 0]), int(lines[i, 1]))

    pt2 = (int(lines[i, 2]), int(lines[i, 3]))

    width = lines[i, 4]

    cv2.line(src, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))

cv2.imwrite(os.path.join(folder, 'cv2_' + imgName.split('.')[0] + '.jpg'), src)