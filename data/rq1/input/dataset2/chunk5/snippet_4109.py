#Source: https://stackoverflow.com/questions/38555408/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
from PIL import Image
from pytesseract import image_to_string
import os.path

if (os.path.exists('image.png')):
    filename = 'image.png'
    image = Image.open(filename)
    image.show()
    s = image_to_string(Image.open(filename))
else:
    print('Does not exist')