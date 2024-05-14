#Source: https://stackoverflow.com/questions/66010232/how-to-resolve-typeerror-expected-str-bytes-or-os-pathlike-object-not-io-buf
root = Tk()
def open_f(): 
    global file
    file = askopenfile(mode ='rb', filetypes =[('All Files','*.*'),
                  ('pdf files', '*.pdf'),('txt Files','*.txt')])
    print('Selected:', file)
    
button1 = Button(root, text ="Select text file",command=open_f)
button1.grid(row=9,column=1,pady=5)
l1=[] 
TextFile = file
# open the file for data processing
with open(TextFile,encoding="utf8") as IpFile:
    for j in IpFile:
        l1.append(str(j).strip())   
       
root.mainloop()