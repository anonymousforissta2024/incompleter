#Source: https://stackoverflow.com/questions/59199749/typeerror-while-trying-to-add-label-widgets-in-tkinter
x = 10
y = 10
i = 0
Labels = ['Name', 'RName', 'Gender', 'Age', 'Cast', 'Add', 'Mob No.', 'Adhar No.']   
for Label in Labels:
    lbp1n = Label(window, text=str(Label))
    lbp1n.place(x=x, y=x)
    x += 10