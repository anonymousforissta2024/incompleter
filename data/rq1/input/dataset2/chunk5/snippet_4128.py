#Source: https://stackoverflow.com/questions/55066875/typeerror-register-user-missing-1-required-positional-argument-self
import tkinter as tk
import os 
import tkinter.messagebox as tm

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

def switch_frame(self, frame_class):
    """Destroys current frame and replaces it with a new one."""
    new_frame = frame_class(self)
    if self._frame is not None:
        self._frame.destroy()
    self._frame = new_frame
    self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Please select an option below").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Register",
                  command=lambda: master.switch_frame(register_screen)).pack()
        tk.Button(self, text="Login",
                  command=lambda: master.switch_frame(login_screen)).pack()

class register_screen(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        global username
        global password
        global username_entry
        global password_entry

        self.username = StringVar()
        self.password = StringVar()

        Label(self, text="Please enter details below").pack()
        Label(self, text="").pack()
        username_lable = Label(self, text="Username * ")
        username_lable.pack()
        username_entry = Entry(self, textvariable=self.username)
        username_entry.pack()
        password_lable = Label(self, text="Password * ")
        password_lable.pack()
        password_entry = Entry(self, textvariable=self.password, show='*')
        password_entry.pack()
        Label(self, text="").pack()
        Button(self, text="Register", width=10, height=1, command = register_user).pack()

class login_screen(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login Page").grid(row=0)

        global username_verify
        global password_verify

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        global username_entry1
        global password_entry1

        tk.Label(self, text = "Username").grid(row = 3, sticky=E)
        username_entry1 = Entry(self,textvariable = username_verify) 
        username_entry1.grid(row = 3, column = 1)

        tk.Label(self, text = "Password").grid(row = 6, sticky=E)
        password_entry1 = Entry(self,show="*",textvariable = password_verify)
        password_entry1.grid(row = 6, column = 1)

        tk.Checkbutton(self, text = "Keep Me Logged In").grid(columnspan = 2) 
        tk.Button(self,text= "Login", command= login_verify).grid(row = 8) 