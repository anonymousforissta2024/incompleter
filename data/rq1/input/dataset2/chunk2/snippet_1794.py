#Source: https://stackoverflow.com/questions/53915690/typeerror-layout-of-the-output-array-img-is-incompatible-with-cvmat-stepndi
import matplotlib.pyplot as plt
import cv2
import numpy as np

black = np.zeros(shape = (512, 512, 3), dtype = np.int64)
cv2.circle(black, center = (100, 100), radius = 50, color = (0, 255, 0), thickness = 10)

plt.imshow(black)