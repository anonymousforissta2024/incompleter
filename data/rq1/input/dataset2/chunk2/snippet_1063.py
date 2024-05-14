#Source: https://stackoverflow.com/questions/38044773/receiving-typeerror-object-new-takes-no-parameters-when-new-not-chang
from Grid import Grid
from tkinter import *

class MainWindow:
    def __init__(self, rows=10, cols=10, wraparound=True, pattern=None):
        self.root = Tk()

        grid_frame = Frame(self.root).pack(side=TOP)
        self.grid = Grid(grid_frame, rows=rows, cols=cols, wraparound=wraparound, pattern=pattern)

        button_frame = Frame(self.root).pack(side=BOTTOM)
        self.time_interval = 1000
        self.start_stop_button = Button(button_frame, text='START', command=self.start_stepper).pack(side=LEFT)
        self.step_button = Button(button_frame, text='STEP', command=self.grid.step)

        self.menubar = Menu(self.root)
        self.menubar.add_command(label='Change Time Interval', command=self.change_time_interval)
        self.root.config(menu=self.menubar)

        self.root.mainloop()

    def change_time_interval(self):
        # Incomplete
        pass

    def start_stepper(self):
        # Incomplete
        pass

    def stop_stepper(self):
        # Incomplete
        pass