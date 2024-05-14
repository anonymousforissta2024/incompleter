#Source: https://stackoverflow.com/questions/52281528/attributeerror-type-object-message-has-no-attribute-get
root = Tk()
frame = Frame(root)
labelText = StringVar()

display = Label(frame, textvariable=labelText)
labelText.set("Connecting to the server...")
display.pack()
frame.pack()
display.update()


def Submit_Message(event):
    Message_Get = Message.get()
    print(Message_Get)

def run_code_1():
    print("Enter Message to send!")
    Message = StringVar()
    Message = Text(root)
    Submit_Data_Button = Button(root, text="Submit")
    Submit_Data_Button.bind("<Button-1>", Submit_Message)
    Submit_Data_Button.pack()
    Message.pack(expand=YES, fill=BOTH)


run_code_1()

root.mainloop()