#Source: https://stackoverflow.com/questions/59117289/python-error-code-attributeerror-tuple-object-has-no-attribute-save
import cv2
from PIL import Image
import numpy as np

def int_to_bin(rgb):
    r, g, b = rgb
    return ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b)) 

def merge_rgb(rgb1, rgb2):
    r1, b1, g1 = rgb1
    r2, b2, g2 = rgb2

    rgb = (r1[:4] + r2[:4], g1[:4] + g2[:4], b1[:4] + b2[:4])

    return rgb

im = "bunga.jpg"
img1 =  Image.open(im,'r')

im2 = "index.jpg"
img2 = Image.open(im2,'r')

pixel_map1 = img1.load()
pixel_map2 = img2.load()

for i in range(img1.size[0]):
    for j in range(img1.size[1]):
        rgb1 = int_to_bin(pixel_map1[i, j])

        if i < img2.size[0] and j < img2.size[1]:
            rgb2 = int_to_bin(pixel_map2[i, j])
            rgb = merge_rgb(rgb1, rgb2)

merged_image = rgb
img = merged_image.save("decode_konversiGreykeBiner.jpg")