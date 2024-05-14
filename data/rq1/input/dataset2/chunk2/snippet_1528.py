#Source: https://stackoverflow.com/questions/66721562/python-multiprocessing-typeerror-cannot-pickle-tkinter-tkapp-object
class experimentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # start experiment on click
        self.button2 = tk.Button(self, text="Ready",
                            command=self.logic)
        self.button2.pack()

    def proc1(self):
        while True:
            print("LOL1")

    def proc2(self):
        while True:
            print("LOL2")

    def proc3(self):
        while True:
            print("LOL3")

    def logic(self):
        t1 = multiprocessing.Process(target=self.proc1)
        t2 = multiprocessing.Process(target=self.proc2)
        t3 = multiprocessing.Process(target=self.proc3)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()