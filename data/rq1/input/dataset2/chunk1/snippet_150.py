#Source: https://stackoverflow.com/questions/50906123/nameerror-name-image-is-not-defined
from PIL import Image
im = Image.open('MobileNet-inference-images/American_Cam.jpg')
im.show()