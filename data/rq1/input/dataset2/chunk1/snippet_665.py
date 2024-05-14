#Source: https://stackoverflow.com/questions/21909435/how-do-i-resolve-this-error-typeerror-argument-1-must-be-pygame-surface-not-p
from PIL import Image
sprites = Image.open('sprites.png')
background.blit(sprites, (0, 0), rect)