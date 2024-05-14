#Source: https://stackoverflow.com/questions/71457635/typeerror-init-takes-from-1-to-2-positional-arguments-but-3-were-given-wh
class MyClass(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        self.frames = {}
        for F in (StartPage, LoginPage, FiltersPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(column=0, row=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()