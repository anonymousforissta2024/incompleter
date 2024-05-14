#Source: https://stackoverflow.com/questions/18937994/python-and-tkinter-nameerror-global-name-roomchange-is-not-defined
from tkinter import *
import tkinter.messagebox

def displayText():
    """ Display the Entry text value. """

    global roomChange


    if roomChange.get().strip() == "":
        tkinter.messagebox.showerror("Invalid Value", "Please enter a valid classroom name.")
    else:
        tkinter.messagebox.showinfo("Temporary Window", "Text value = " + roomChange.get().strip()) 

def roomChanger():

    chrm = Tk()
    chrm.title("Change Room")
    chrm.wm_iconbitmap('./Includes/icon.ico')
    chrm["padx"] = 40
    chrm["pady"] = 20       

    # Create a text frame to hold the text Label and the Entry widget
    textFrame = Frame(chrm)

    #Create a Label in textFrame
    roomChangeLabel = Label(textFrame)
    roomChangeLabel["text"] = "Enter name of classroom: "
    roomChangeLabel.pack(side=LEFT)

    # Create an Entry Widget in textFrame
    roomChange = Entry(textFrame)
    roomChange["width"] = 50
    roomChange.pack(side=LEFT)

    textFrame.pack()

    roomChangeButton = Button(chrm, text="Submit", command=displayText)
    roomChangeButton.pack() 

    chrm.mainloop()


testButton = Button(window, text='Change Room', command=roomChanger)
testButton.place(x = 825, y = 360)