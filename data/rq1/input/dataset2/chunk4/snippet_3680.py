#Source: https://stackoverflow.com/questions/56955112/nameerror-name-label-is-not-definednameerror-name-label-is-not-defined
def register_user():

    global username
    global password
    global username_entry
    global password_entry

#Username e password
    username_info = username.get()
    password_info = password.get()

#aprire file in write mode
    file = open(username_info, "w")

#scrittura info nel file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

Label(register_screen, text="Registrazione avvenuta con successo", fg="green", font=("Lemon/Milk", 11)).pack
Button(text="Login", height="2", width="30", command = login).pack