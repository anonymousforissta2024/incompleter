#Source: https://stackoverflow.com/questions/45871308/typeerror-frame-object-is-not-callable-error
import pandas
from tkinter import *
#assigns a dataframe variable
summer17=pandas.read_excel("summer17.xlsx","list")

window=Tk()#Start of the main window
row_widget = Frame(window)#Creates a frame or "megawidget"
row_widget.grid()
#Variaous variables for widget parameters
tw_height = 1.5
tw_width1 = 30
tw_width2 = 5
brew_row = 14
#Text blocks for megawidget
t1=Text(row_widget,height=tw_height,width=tw_width1)
t1.grid(row=0,column=0)
t1.insert(END,summer17.iloc[brew_row,0])

t2=Text(row_widget,height=tw_height,width=tw_width1)
t2.grid(row=0,column=1)
t2.insert(END,summer17.iloc[brew_row,1])

t3=Text(row_widget,height=tw_height,width=tw_width2)
t3.grid(row=0,column=2)
t3.insert(END,summer17.iloc[brew_row,2])

t4=Text(row_widget,height=tw_height,width=tw_width2)
t4.grid(row=0,column=3)
t4.insert(END,summer17.iloc[brew_row,3])

t5=Text(row_widget,height=tw_height,width=tw_width2)
t5.grid(row=0,column=4)
t5.insert(END,summer17.iloc[brew_row,4])

t6=Text(row_widget,height=tw_height,width=tw_width2)
t6.grid(row=0,column=5)
t6.insert(END,summer17.iloc[brew_row,5])
#for loop to create new instances of the megawidget
for i in range(len(summer17.index)):
    row = row_widget(Frame)
    row.grid(row=i,column=0)

window.mainloop()