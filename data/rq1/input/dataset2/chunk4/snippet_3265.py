#Source: https://stackoverflow.com/questions/74534074/typeerror-expected-str-bytes-or-os-pathlike-object-not-function-error-in-my-p
class Something:
    def load_key(self):
        filename = self.browse_files
        with open(filename, "rb") as f:
            self.key = f.read()

  
    def browse_files():
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        return filename


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
   
        self.button2 = customtkinter.CTkButton(master=self, text="Load a key",              command=Something.load_key(Something), width=450, height=60)
        self.button2.pack(pady=10, padx=50)


if __name__ == "__main__":
    app = App()
    app.mainloop()