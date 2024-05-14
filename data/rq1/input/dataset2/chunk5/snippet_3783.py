#Source: https://stackoverflow.com/questions/41368728/typeerror-a-bytes-like-object-is-required-not-str-in-python-3-5-2-and-pytess
# -*- coding: utf-8 -*-

try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract


print(pytesseract.image_to_string(Image.open('d:/testimages/name.gif'), lang='chi_sim'))
print(pytesseract.image_to_string(Image.open('d:/testimages/mobile.gif')))