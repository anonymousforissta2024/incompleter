#Source: https://stackoverflow.com/questions/69653682/typeerror-return-entry-takes-0-positional-arguments-but-1-was-given-the-conv
def return_entry() :
    content = ew.get()
    print(content)

ew = Entry(root, font = myfont, width = 30)
ew.place(x = 170, y = 100)
ew.bind('<Return>', return_entry)