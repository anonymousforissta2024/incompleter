#Source: https://stackoverflow.com/questions/56955112/nameerror-name-label-is-not-definednameerror-name-label-is-not-defined
from tkinter import *
import runpy

file_globals = runpy.run_path("Register_user().py")
file_globals = runpy.run_path("register().py")


def main_account_screen():

    global main_screen
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen = Tk() #Crea finetra gui
    main_screen.geometry("300x250")
    main_screen.title("Login") #Titolo gui


#Form
Label(text="Login o Registrati", bg="blue", width="300", height="2", font=("Lemon/Milk", 13)).pack()
Label(text="").pack()

#Login Button
Button(text="Login", height="2", width="30").pack()
Label(text="").pack()

#Register Button
Button(text="Registrati", height="2", width="30").pack()

main_screen.mainloop() #Starta la GUI

main_account_screen() #Chiama la funzione