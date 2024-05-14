#Source: https://stackoverflow.com/questions/57208264/nameerror-name-ptime-is-not-defined-using-tkinter-scale-scroller
def set_Tk_var():
    global Ptime
    Ptime = tk.DoubleVar()
    global Pspeed
    Pspeed = tk.StringVar()

text = "play: timecode: 00:00:0" + str(Ptime) + ";00 \\nc"
def IRplay():
    print('testguiPAGE_support.IRplay')
    session.write(b"stop\n")
    session.write( text.encode() )
    sys.stdout.flush()