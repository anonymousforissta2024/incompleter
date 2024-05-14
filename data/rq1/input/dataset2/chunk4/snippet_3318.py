#Source: https://stackoverflow.com/questions/75709003/attributeerror-module-emotions-has-no-attribute-emotion
from greetings import greeting
from emotions import emotion

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme('blue')

chosen_greeting = greeting.choose_greeting()

app = customtkinter.CTk() # Create screen
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}")
app.title("Login")


def check_emotion():
    found_emotion = emotion.check()
    if found_emotion == '0004302X':
        text = chat.cget("text")
        text = emotion.not_found()
        chat.configure(text=text)
    elif found_emotion == '00492X':
        the_emotion = emotion.goodBad()
        if the_emotion == 'bad':
            print("bad")
        elif the_emotion == 'good':
            print('good')
        elif the_emotion == 'meh':
            print('meh')
        else:
            print('error')

def HomeAI():
    global chat
    global text_given

    app.destroy()
    home = customtkinter.CTk()
    home.geometry(f"{screen_width}x{screen_height}")
    home.title('AI screen')

    #AIChat = customtkinter.CTkScrollableFrame(master=home, width=1000, height=900)
    #AIChat.place(rely=0.45, relx=0.5, anchor=tkinter.CENTER)

    chat = customtkinter.CTkLabel(master=home, text="", font=('', 20))
    chat.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

    chat.cget("text")
    chat.configure(text=chosen_greeting)

    text_given = customtkinter.CTkEntry(master=home, width=500, placeholder_text="Enter message", font=('', 20))
    text_given.place(relx=0.85, rely=0.9, anchor=tkinter.CENTER)

    submit = customtkinter.CTkButton(master=home, width=30, text="Enter", font=('', 20), command=check_emotion)
    submit.place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)




    home.mainloop()