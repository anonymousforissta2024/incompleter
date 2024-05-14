#Source: https://stackoverflow.com/questions/76879501/tkinter-super-init-produces-attributeerror-while-tk-entry-init-do
class DirEntry(tk.Entry):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(self, parent, *args, **kwargs)