#Source: https://stackoverflow.com/questions/56368746/typeerror-entry-object-is-not-callable
painter = {}
title = {}
names = []
pnttoedit = ''
copyat = 1

def saveedit(): 
    w = str(title[pnttoedit]) + " (" + str(copyat) + ")"
    names.append(w)
    v = painter[pnttoedit]
    painter[w] = v
    messagebox.showinfo("Painter's Inventory", "Copy of " + str(pnttoedit) + " created.")
    print(str(pnttoedit))

def grabpaintingname():
     global pnttoedit
     pnttoedit = tvkare.get()
     saveedit()

tvkare = StringVar(editers)
tvkare.set(names[0])
e2 = OptionMenu(mainframe, tvkare, *names)
e2.grid(row=3, column=1)
def change_dropdown(*args):
    pnttoedit = tvkare.get()