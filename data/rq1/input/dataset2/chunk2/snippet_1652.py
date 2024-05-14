#Source: https://stackoverflow.com/questions/55794829/how-to-solve-the-error-attributeerror-type-object-image-has-no-attribute-op
from tkinter import *  
from PIL import ImageTk,Image  

def plot_best_batsmen():
    best_batsmen = dataset.loc[dataset.loc[dataset['Innings']>=15,'Average'].idxmax(),'Names']
    message = ("The best Batsman of the Tournament could possibly be: ", best_batsmen)
    canvas_width = 500
    canvas_height = 500
    root = Tk()
    root.geometry("600x600")
    root.title("New Window")
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.create_text(1, 10, anchor=W, text=message)
    img = ImageTk.PhotoImage(Image.open("prediction.jpg"))
    canvas.create_image(20, 20, anchor=NW, image=img)
    canvas.image = img
    canvas.pack()
    root.mainloop()