#Source: https://stackoverflow.com/questions/67425476/how-to-get-rid-of-the-resize-attribute-error
import tkinter as tk
from PIL import Image, ImageTk

image1 = Image.open("enseigne.JPEG")
image1= ImageTk.PhotoImage(image1)
imageresize = image1.thumbnail((500,500), Image.ANTIALIAS)
imageresize = ImageTk.PhotoImage(imageresize)
limage = tk.Label(app, image=imageresize)