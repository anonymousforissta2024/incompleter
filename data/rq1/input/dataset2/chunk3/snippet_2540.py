#Source: https://stackoverflow.com/questions/55538090/typeerror-index-takes-2-positional-arguments-but-3-were-given
def calendar():
    def print_sel():
        dob.index(INSERT, cal.selection_get())

    top = Toplevel(root)
    top.title("Select Registration Date")

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2019, month=4, day=4)

    cal.pack(fill="both", expand=True)

    Button(top, text="ok", command=print_sel).pack()


dob=Entry(Registration_Frame,style='TEntry')
dob.grid(row=3,column=1,columnspan=2,sticky=NSEW)

Button(Registration_Frame, text='Select',command=calendar,width=5,style='TButton').grid(row=3,column=3)