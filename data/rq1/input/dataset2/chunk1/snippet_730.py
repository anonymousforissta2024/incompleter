#Source: https://stackoverflow.com/questions/65637744/attributeerror-module-skimage-has-no-attribute-filters
import cv2
import numpy as np
from PIL import Image
import skimage

my_image = cv2.imread('my_image.jpeg', 1)

gray = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
b = skimage.filters.threshold_local(gray,19,offset=10)
b = Image.fromarray(b)
b = b.convert("L")
b.save('adaptive_output.png')