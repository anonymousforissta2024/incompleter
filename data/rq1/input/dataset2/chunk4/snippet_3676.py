#Source: https://stackoverflow.com/questions/61497467/attributeerror-module-numpy-has-no-attribute-asarray
from PIL import Image
import numpy as np
im = Image.open("photo.jpg", "r")
data = np.asarray(im)
print(data)