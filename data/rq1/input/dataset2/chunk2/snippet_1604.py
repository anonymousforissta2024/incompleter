#Source: https://stackoverflow.com/questions/33762610/pytesseract-error-on-python3-filenotfounderror-winerror-2
import pytesseract
from PIL import Image

img = Image.open('test.png')
print(pytesseract.image_to_string(img))