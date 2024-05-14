#Source: https://stackoverflow.com/questions/59990889/i-keep-getting-typeerror-template-takes-no-arguments
selectedVersion = tk.StringVar()
selectedVersion.set(templateVersion[0])
#Template Menu
templateMenu = OptionMenu(frameTemp, selectedVersion, *templateVersion)
templateMenu.pack()

selectBtn = tk.Button(frameTemp, text = "Select", command = selectVersion)
selectBtn.pack()

version = tk.StringVar()

#label

tempLbl = Label(frameTemp, textvariable = version)
tempLbl.pack()

win.mainloop()