#Source: https://stackoverflow.com/questions/60978050/python-script-works-fine-independently-however-when-called-from-an-external-sc
from tkinter import *

from tkinter import messagebox 


tasks_list = [] 

counter = 1

# Function for checking input error when 
# empty input is given in task field 
def inputError() : 


    if enterTaskField.get() == "" : 


        messagebox.showerror("Input Error") 

        return 0

    return 1