#Source: https://stackoverflow.com/questions/33724910/nameerror-with-defining-command-on-python
class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="blue")
        button = tk.Button(self, text="Main Menu", font=LARGE_FONT, background="white",
                           command=lambda: controller.show_frame(Main))
        button.place(relx=0.83, rely=0.92)

        button4 = tk.Button(self, text="Start Game", font=LARGE_FONT, background="white",
                           command=self.time_start)
        button4.place(relx=0.42, rely=0.8, relheight=0.1, relwidth=0.2)

    def time_start(self):
        timelabel = tk.Label(self, text="Good luck!", font=LARGE_FONT, background="blue")
        timelabel.place(relx=0.42, rely=0.8, relheight=0.1, relwidth=0.2)

        x = int(random.uniform(1,10))
        y = int(random.uniform(50,100))
        z = int(random.uniform(10,50))
        qlabel = tk.Label(self, text= (x,"+",y,"+",z,"=",), font=LARGE_FONT, bg="blue")
        qlabel.pack()

##        entrylabel = tk.Label(self, text="Answer:", font=LARGE_FONT, background="blue")
##        entrylabel.pack()

        e1 = tk.Entry(self)
        e1.pack()

        ebutton = tk.Button(self, text="Done", font=LARGE_FONT, background="white",
                            command=submit_answer)
        ebutton.pack()

    def submit_answer(self):
        a = (x+y+z)
        if int(e1.get()) == a:
            answerlabel = tk.Label(self, text="Correct!", font=LARGE_FONT, background="blue")
            answerlable.pack()
        else:
            answerlabel = tk.Label(self, text="Incorrect!", font=LARGE_FONT, background="blue")
            answerlable.pack()

        self.label = tk.Label(self, text="", width=10, font=LARGE_FONT)
        self.label.place(relx=0.1, rely=0.1)
        self.remaining = 0
        self.countdown(5)