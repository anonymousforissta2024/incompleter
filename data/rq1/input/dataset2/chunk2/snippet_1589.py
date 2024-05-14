#Source: https://stackoverflow.com/questions/66721562/python-multiprocessing-typeerror-cannot-pickle-tkinter-tkapp-object
class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.attributes('-fullscreen', True) 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (startPage.startPage, experimentPage.experimentPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(startPage.startPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

app = Main()
app.mainloop()