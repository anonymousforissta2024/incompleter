#Source: https://stackoverflow.com/questions/53748877/python-3-for-loop-typeerror-int-object-is-not-iterable
import numpy as np
import math
from PIL import Image
from PIL import ImageDraw

im = Image.open('harita2.png').convert("RGB")
npimage = np.array(im)
g1= np.array([93,95,95],dtype=np.uint8)
g2= np.array([54,55,55],dtype=np.uint8)
g3= np.array([84,86,86],dtype=np.uint8)
s= np.array([0,0,0],dtype=np.uint8)
#print(g1)
x1,y1=np.where(np.all((npimage==g1),axis=-1))
print(x1)
tt = x1.size
tt = int(tt)
print(tt)
print(x1[15])
print(y1[15])   

for vvv in tt:
    idraw = ImageDraw.Draw(im)
    idraw.point((x1[vvv],y1[vvv]),s)

im.save('boyatest.png')