#Source: https://stackoverflow.com/questions/74967046/how-can-i-import-a-function-into-class-of-an-external-file-nameerror-name-cli
import tkinter as tk
from tkinter import ttk

class Page1(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        Checkbutton1 = tk.IntVar()

        def Button1_func():
            x = "test"
            return x
  
        Button1 = tk.Checkbutton(self, text = "Checkbox1", variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 1,
                                 bg="white", foreground='black', activebackground="white", highlightthickness = 0,
                                 command=lambda: clicked(Checkbutton1.get(), Button1_func))
        Button1.place(x=10, y=30)