#Source: https://stackoverflow.com/questions/61617089/i-keep-getting-this-error-in-python3-typeerror-an-integer-is-required-got-typ
from tkinter import *
from os import *

nameFile = open("Names.txt", O_APPEND)
passwordFile = open("Passwords.txt", O_APPEND)

def SignUp():

    def storeData():

        name = signupNameEntry.get()
        password = signupPasswordEntry.get()
        rpassword = signupRPasswordEntry.get()

        print(name)
        print(password)
        print(rpassword)
        print(type(name))
        print(type(password))

        if password == rpassword:
            print("passwords match")
            nameFile = open("Names.txt", "a")
            passwordFile = open("Passwords.txt", "a")
            passwordFile.write(password)
            nameFile.write(name)
            passwordFile.close()
            nameFile.close()

        else:
            print("passwords don't match")


    signup = Toplevel()
    signup.title("Sign Up")

    Label(signup, text="Name", pady=5, padx=5).grid(row=1, column=1)
    Label(signup, text="Password", pady=5, padx=5).grid(row=2, column=1)
    Label(signup, text="Repeat\nPassword").grid(row=3, column=1)
    signupNameEntry = Entry(signup)
    signupNameEntry.grid(row=1, column=2)
    signupPasswordEntry = Entry(signup)
    signupPasswordEntry.grid(row=2, column=2)
    signupRPasswordEntry = Entry(signup)
    signupRPasswordEntry.grid(row=3, column=2)
    signupButton = Button(signup, text="Sign Up", command=storeData, pady=5, padx=5).grid(row=4, column=2)

    signup.mainloop()