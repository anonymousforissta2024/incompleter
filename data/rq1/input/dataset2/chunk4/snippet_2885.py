#Source: https://stackoverflow.com/questions/29835061/typeerror-type-str-doesnt-support-the-buffer-api-when-using-str-rstrip
from tkinter import ttk
from tkinter import *
import tkinter, imaplib,email
def signin(w,x,s):
        tkgui = tkinter.Tk()
        tkgui.title('Inbox %s'%w)
        mail=imaplib.IMAP4_SSL(('%s'%s),993)
        mail.login(('%s'%w ), ('%s'%x))
        mail.list()
        mail.select("INBOX")
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        tree = ttk.Treeview(tkgui)
        for i in range(-1,0):       
                result, data = mail.fetch(id_list[i], '(RFC822)')
                raw_email = data[0][1]
                d = email.message_from_bytes(raw_email)
                tree.insert('',0,value=(d['Date'],d['From'],d['Subject']))
        tree['columns']=['Date','From','Subject']
        r=raw_email.rstrip('\r\n')
        print(r)
        for col in tree['columns']:
            tree.heading(col,text=col)
        tree.pack(side=TOP,fill=BOTH,expand=1)
        tkgui.mainloop()