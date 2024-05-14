#Source: https://stackoverflow.com/questions/63742441/how-to-deal-with-attributeerror-tkinter-tkapp-object-has-no-attribute-mess
greet_button = Button(
    table,
    text = 'Yes',
    width = 20,
    height = 2,
    bg = 'yellow',
    fg = 'red',
    command = table.messagebox.showinfo(title='Hello', message='Hello!')
)