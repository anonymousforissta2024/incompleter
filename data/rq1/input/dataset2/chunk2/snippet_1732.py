#Source: https://stackoverflow.com/questions/64341578/attributeerror-choosebook-object-has-no-attribute-txtrd
class ChooseBook():

    bookprice=2
    def getqty(self, sv):
        if self.txtbookqty.get()=="":
            self.qty=0
        else:
        
            self.qty=int(self.sv.get())
            self.txtbookprice.delete(0,END)
            #print(self.qty)
            self.txtbookprice.insert(0,self.qty*self.bookprice)

    def on_CPOname_change(self,value,op,op2):
        stname=self.comboBookname.get()
        name=stname[1:-1]
        book_data=Fun_Select("SELECT book_price FROM book_record WHERE book_name='"+name+"'")
        #print(book_data)
        self.bookprice=int(book_data[0][0])

    def on_date_change(self,day):
        if self.txtdaysborrowed.get()=="":
            self.dayadd=0

        else:
            self.dayadd=int(self.day.get())
            date=self.txtborrowdate.get()
            self.dayindate=int(date[8:10])
            self.yearindate=int(date[0:4])
            self.monthindate=int(date[5:7])
            if self.dayindate+self.dayadd > 31:
                self.monthindate=self.monthindate+1
                if self.monthindate > 12:
                    self.yearindate+=1
            self.txtrd.insert(0,self.dayindate+'-'+self.monthindate+'-'+self.yearindate)
            


    def __init__(self):

        
        
        today_date=datetime.date.today()
        win=Tk()
        win.title("Choose book type")
        win.geometry("600x800")
        v=StringVar()
        d=StringVar()
        v.trace('w', self.on_CPOname_change)
        self.day=StringVar()
        self.day.trace('w',lambda name, index, mode, day=self.day: self.on_date_change(day))
        self.sv = StringVar()
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.getqty(sv))

        Label(win,text="Choose Book Name").grid(row=0,column=0,padx="1.5c",pady="1c")
        Label(win,text="Enter Book Quantity").grid(row=1,column=0,padx="1.5c",pady="1c")
        Label(win,text="Total Book Price").grid(row=2,column=0,padx="1.5c",pady="1c")
        Label(win,text="Borrowed Date").grid(row=3,column=0,padx="1.5c",pady="1c")
        Label(win,text="Days borrowed").grid(row=4,column=0,padx="1.5c",pady="1c")
        Label(win,text="Return Date").grid(row=5,column=0,padx="1.5c",pady="1c")
        Label(win,text="Choose Employee Name").grid(row=6,column=0,padx="1.5c",pady="1c")
        Label(win,text="Choose Customer Name").grid(row=7,column=0,padx="1.5c",pady="1c")
        
        #bookname
        self.comboBookname=ttk.Combobox(win, textvar=v)
        self.comboBookname["values"]=Fun_Select("SELECT book_name FROM book_record")
        self.comboBookname.grid(row=0,column=1,pady="1c")
        #bookqty
        self.txtbookqty=Entry(win,textvariable=self.sv)
        self.txtbookqty.grid(row=1,column=1,pady="1c")
        #bookprice
        self.txtbookprice=Entry(win)
        self.txtbookprice.grid(row=2,column=1,pady="1c")
        #borrowdate
        self.txtborrowdate=Entry(win,textvariable=d,state=DISABLED)
        d.set(today_date)
        self.txtborrowdate.grid(row=3,column=1,pady="1c")
        #daysborrowed
        self.txtdaysborrowed=Entry(win,textvariable=self.day)
        self.day.set(0)
        self.txtdaysborrowed.grid(row=4,column=1,pady="1c")
        #returndate
        self.txtrd=Entry(win)
        self.txtrd.grid(row=5,column=1,pady="1c")
        #employeename
        self.comboEmployeename=ttk.Combobox(win)
        self.comboEmployeename["values"]=Fun_Select("SELECT employee_name FROM employees")
        self.comboEmployeename.grid(row=6,column=1,pady="1c")
        #customername
        self.comboCustomername=ttk.Combobox(win)
        self.comboCustomername["values"]=Fun_Select("SELECT customer_name FROM customers")
        self.comboCustomername.grid(row=7,column=1,pady="1c")
        
        

        Button(win,text="Exit",width=10,command=win.destroy).grid(row=8,column=0,padx="1.5c",pady="1c")
        Button(win,text="Save",width=10,command=None).grid(row=8,column=1,padx="1.5c",pady="1c")
                                    
        win.mainloop()
ChooseBook()