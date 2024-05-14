#Source: https://stackoverflow.com/questions/29311509/positional-argument-typeerror-python-tkinter
from tkinter import *

class Search(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.bind("<Return>", self.search_button)

        self.search_bar = Frame(self, bg="blue")
        self.search_bar.pack(side=TOP, fill=X)
        self.index = Frame(self, width=100)
        self.index.pack(side=LEFT)
        self.content = Frame(self, bg="red")
        self.content.pack(side=LEFT, fill=X)
        self.status_bar = Frame(self, bg="green")
        self.status_bar.pack(side=BOTTOM, fill=X)

        self.entry = Entry(self.search_bar)
        self.entry.pack(side=LEFT, padx=4, pady=4)
        self.search = Button(self.search_bar, text="Search", command=self.search_button)
        self.search.pack(side=LEFT)
        self.content = Label(self.content, text="DUPA")
        self.content.pack(side=LEFT)
        self.status_bar = Label(self.status_bar, text="DUPA")
        self.status_bar.pack(side=LEFT)

    def search_button(self):
        (self.entry.get())
        if self.entry.get() == 'example1':
            print("lorem ipsum")