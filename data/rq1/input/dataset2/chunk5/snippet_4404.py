#Source: https://stackoverflow.com/questions/44469465/attributeerror-nonetype-object-has-no-attribute-root-my-case-is-different
from tkinter import*
decision=0
fs = IntVar()
def coverscreen():
    slide=Tk() #Init window
    slide.title('The Castle of Redemption BETA') #Give window a title
    frame=Frame(slide)
    btn1=Button(slide,text='Start Game',command=slide.destroy) #Init 1st            button
    fsbox=Checkbutton(frame,text='Fullscreen',\
    variable=fs, onvalue=1,offvalue=0)
    img=PhotoImage(file='cover.gif') # Init picture
    label = Label(image=img) # Init label that contains picture
    label.image = img # keep a reference!
    label.pack() # Places the label on the window
    btn1.pack(side=BOTTOM,pady=5) # Places the 1st button on the window
    fsbox.pack()
    frame.pack(padx=50,pady=50)
    slide.mainloop() # Starts the window
def page(name,b1,b2,write,f,fscreen):
    slide=Tk() #Init window
    if fscreen == 1:
        slide.overrideredirect(True)
        slide.geometry("{0}x{1}+0+0".format(slide.winfo_screenwidth(),     slide.winfo_screenheight()))
    slide.title(name) #Give window a title
    btn1=Button(slide,text=b1,command=slide.destroy) #Init 1st button
    btn2=Button(slide,text=b2,command=slide.destroy) #Init 2nd button
    txt=Label(slide,text=write)# Init story text
    img=PhotoImage(file=f) # Init picture
    label = Label(image=img) # Init label that contains picture
    label.image = img # keep a reference!
    label.pack() # Places the label on the window
    btn1.pack(side=BOTTOM,pady=5) # Places the 1st button on the window
    btn2.pack(side=BOTTOM,pady=5) # Places the 2nd button on the window
    txt.pack(side=TOP,pady=5) # Places the text on the window
    slide.mainloop() # Starts the window
coverscreen()
page('Start','Continue','Go Back','Example Story Text.','cover.gif',fs.get()) #Example of the created function 'page'