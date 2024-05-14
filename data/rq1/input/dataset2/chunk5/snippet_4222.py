#Source: https://stackoverflow.com/questions/61327187/error-in-python3-typeerror-module-object-is-not-callable
import pyperclip
import tkinter as Tk
while True:
 r = Tk()
 r.withdraw()
 try:
      selection = r.selection.get(selection="CLIPBOARD")
 except tk.TclError:
      selection = None
      sleep(0.1)

 try:
     selection = r.selection.get(selection="CLIPBOARD")
 except tk.TclError:
     selection = None
     r.clipboard_clear()
     if len(result) > 10:
       pyperclip.copy("aaa")