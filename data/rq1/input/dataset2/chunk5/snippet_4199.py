#Source: https://stackoverflow.com/questions/60978050/python-script-works-fine-independently-however-when-called-from-an-external-sc
toDoBtn = tk.Button(self, text = "To Do List",
                command=lambda: exec(open("ToDo.py").read()))