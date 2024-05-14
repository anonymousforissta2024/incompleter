#Source: https://stackoverflow.com/questions/62584911/opening-an-image-using-imagetk-in-pillow-causing-an-attributeerror-and-runtimeer
from PIL import Image, ImageTk

image = Image.open("0.gif")
photo = ImageTk.PhotoImage(image)