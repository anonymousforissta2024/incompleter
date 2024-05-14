#Source: https://stackoverflow.com/questions/63275396/nameerror-name-ntxtbox-is-not-defined-even-though-ntxtbox-is-a-global-variab
from Tkinter import *

admin = Tk()
def button(an):
    print(an)
    print('het')

b = Button(admin, text='as', command=button('hey'))
b.pack()
mainloop()