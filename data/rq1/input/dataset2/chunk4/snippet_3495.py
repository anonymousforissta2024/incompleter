#Source: https://stackoverflow.com/questions/36001867/nameerror-name-clear-message-is-not-defined
from Tkinter import *
import tkinter as tk   # python3

TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where I stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage,StorageOrMotor,Storage,Motor):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):

    global user_key
    global psw_key
    user_key=""
    psw_key=""

#Here is the defined for clear_message `def`   
    def clear_message():
        user_key.delete(0, 'END')
        psw_key.delete(0, 'END')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Username = tk.Label(self, text="Username:",font=("Helvetica", "20","bold"))
        Username.grid(row=2, column=3,columnspan=2)
        Password = tk.Label(self, text="Password:",font=("Helvetica", "20","bold"))
        Password.grid(row=3, column=3,columnspan=2)

#............        
        Username_key = tk.Entry(self, textvariable = user_key, width=19, font=("Helvetica", "15"))
        Username_key.grid(row=2, column=5,columnspan=5)
        Password_key = tk.Entry(self, textvariable = psw_key, width=19, font=("Helvetica", "15"))
        Password_key.grid(row=3, column=5,columnspan=5)
        log_in = tk.Button(self, width=7, text="Log In", command=lambda: controller.show_frame("StorageOrMotor"))
        log_in.grid(row=5,column=8,columnspan=2)
#............`I try to create a clear button`
        Clear = tk.Button(self, width=7, text=" Clear " ,command=lambda:clear_message())
        Clear.grid(row=5,column=5,columnspan=2)