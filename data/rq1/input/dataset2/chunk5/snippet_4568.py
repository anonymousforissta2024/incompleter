#Source: https://stackoverflow.com/questions/53278224/python-type-error-while-using-exec-for-creating-tkinter-checkbutton
for ii,j in zip(range(len(files_list)),range(1,len(files_list)+1)):
    exec("var%i=StringVar()"%j)
    exec("ch%i = Checkbutton(text=files_list[ii],variable=var%i)"%j%j)
    exec("ch%i.grid(row=ii, column=0, sticky=W)"%j)