#Source: https://stackoverflow.com/questions/71457635/typeerror-init-takes-from-1-to-2-positional-arguments-but-3-were-given-wh
class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.startMenu()

    def startMenu(self):
        heading = Label(self, text="My App", font=('Arial', 30))
        heading.grid(column=0, row=0)

        start_button = Button(self, text="Start", font='Arial 16', width=8, command=lambda: self.controller.show_frame(LoginPage))
        start_button.grid(column=0, row=1)

        exit_button = Button(self, text="Exit", font='Arial 16', width=8, command=self.controller.destroy)
        exit_button.grid(column=1, row=1)