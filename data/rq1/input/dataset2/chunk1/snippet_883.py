#Source: https://stackoverflow.com/questions/76254003/wndproc-return-value-cannot-be-converted-to-lresult-typeerror-wparam-is-simple
myschedule = []

def func():
    import schedule
    import time
    import win10toast


    noti=win10toast.ToastNotifier()

    choice="yes"
    while choice=="yes":
        title=input("enter the title")
        message=input("enter the message")
        tim=input("enter the time")
        ms=[title,message,tim]
        myschedule.append(ms)

        choice = input("enter your choice:")
        if choice == "yes":
            title = input("enter the title")
            message = input("enter the message")
            tim = input("enter the time")
            ms = [title, message, tim]
            myschedule.append(ms)
            choice = input("enter your choice:")


        else:
            pass


    for i in myschedule:

        def functionmaker():
            noti.show_toast(i[0],i[1],duration=12)

        schedule.every().day.at(i[2]).do(functionmaker)

        while True:
            schedule.run_pending()

func()