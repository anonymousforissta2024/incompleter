#Source: https://stackoverflow.com/questions/49861600/why-am-i-getting-this-class-tkinter-entry-get-attributeerror-error
class asd:

    def gui(self, guiwindow, labelplacex, labelplacey, textx, texty, entryx, entryy):
        self.root = tk
        self.image = tk.PhotoImage(file=aimage_path)
        self.label = tk.Label(image=self.image)
        self.label.pack()
        self.label.place(x=labelplacex , y=labelplacey)
        self.text = Label(guiawindow, text="Code:")
        self.text.pack()
        self.text.place(x = textx,y = texty)
        self.entry = Entry(guiwindow)
        self.entry.pack()
        self.entry.place(x = entryx,y = entryy)
        self.button = Button(Tk(), text="Back Menu", command=self.asdfg)
        self.button.pack()
        self.root.mainloop()

asd.gui.entry.get()