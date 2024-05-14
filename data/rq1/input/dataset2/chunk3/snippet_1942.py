#Source: https://stackoverflow.com/questions/50538447/attributeerror-module-zbar-has-no-attribute-imagescanner
import pyqrcode
from qrtools import qrtools
from PIL import Image
import zbar
qr = pyqrcode.create("She got two litle horns and they get me a litle bit")
qr.png("horn.png", scale=6)
qr = qrtools.QR()
scanner = zbar.Scanner()
qr.decode("horn.png")
print(qr.data)