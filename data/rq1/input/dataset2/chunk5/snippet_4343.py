#Source: https://stackoverflow.com/questions/60090995/typeerror-an-integer-is-required-got-type-tuple
import cv2
import numpy as np
import pytesseract
from langdetect import detect_langs
from pytesseract import *
from flask import Flask,request
import requests 

try:
    from PIL import Image
except ImportError:
    import Image

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


img = Image.open('G:/Agrima/example_code_API/OCR/FDA.png')

#h, w, c = img.shape

d = pytesseract.image_to_data(img,output_type=Output.DICT)


detected_ocr = image_to_string(img)
points = []
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i],d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        mark = {'x':x,'y':y,'width':w,'height':h}
        points.append({'mark':mark})

# print(points)
cv2.imshow('img', img)
cv2.waitKey(0)