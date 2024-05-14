#Source: https://stackoverflow.com/questions/33987368/custom-float-entry-for-tkinter-throwing-attribute-error-upon-deleting-contents
class FloatEntry(tk.Entry):

    def __init__(self, master, default=0.0, **kwargs):

        tk.Entry.__init__(self, master, **kwargs)
        self.default = default
        self.value = self.default
        self.float = tk.DoubleVar()
        self.float.set(self.value)
        self.float.trace("w", self.__callback)
        self.config(textvariable=self.float)

    def __callback(self, *dummy):
        value = self.float.get()
        new_value = self.validate(value)
        if new_value is None:
            self.float.set(self.default)
        elif new_value != value:
            self.value = new_value
            self.float.set(self.new_value)
        else:
            self.value = value

    def validate(self, value):
        try:
            if value:
                value = float(value)
            return value
        except ValueError:
            return None