#Source: https://stackoverflow.com/questions/38044773/receiving-typeerror-object-new-takes-no-parameters-when-new-not-chang
from random import randint
from tkinter import *

class Cell:
    def __init__(self, master, state=None):
        if state is None:
            state = randint(0,2)
        self.state = state
        self.next_state = state
        self.button = Button(master, width=2, height=1, bg = 'black' if self.state == 1 else 'white').pack(side=LEFT)

    def __del__(self):
        self.button.destroy()

    def set_next_state(self, neighbours):
        if self.state == 1:
            self.next_state = 0 if neighbours < 2 or neighbours > 3 else 1
        else:
            self.next_state = 1 if neighbours == 3 else 0

    def update(self):
        self.state = self.next_state
        self.button.config( bg = 'black' if self.state == 1 else 'white')