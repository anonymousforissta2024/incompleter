#Source: https://stackoverflow.com/questions/77208733/import-widgets-into-a-function-from-a-class-in-another-file-nameerror-name-te
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Page1(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.textbox1 = ttk.Entry(self, width=7)
        self.textbox1.place(x=10, y=10)

        self.textbox2 = ttk.Entry(self, width=7)
        self.textbox2.place(x=10, y=40)