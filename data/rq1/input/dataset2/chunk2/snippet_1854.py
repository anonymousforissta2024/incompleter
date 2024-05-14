#Source: https://stackoverflow.com/questions/67182310/typeerror-pack-configure-missing-1-required-positional-argument-self
my_window = Tk()
my_canvas_1 = Canvas(my_window, height=500, width=500, bg='white')
my_canvas_2 = Canvas(my_window, height=500, width=250, bg='white')
my_canvas_1.grid(row=0, column=0)
my_canvas_2.grid(row=0, column=1)
Canvas.pack()
my_window.mainloop() 