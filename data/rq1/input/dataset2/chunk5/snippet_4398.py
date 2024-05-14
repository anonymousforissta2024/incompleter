#Source: https://stackoverflow.com/questions/57934091/attributeerror-tkinter-tkapp-object-has-no-attribute-text-in-tkinter
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk().__init__(self, *args, **kwargs)

        super().__init__()

        self.title('AccWeather')
        self.geometry('600x500')