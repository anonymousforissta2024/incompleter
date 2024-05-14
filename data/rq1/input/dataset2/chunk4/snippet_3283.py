#Source: https://stackoverflow.com/questions/75979136/tkinter-updating-label-fails-with-attributeerror-frame-object-has-no-attribu
#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import serial
Arduino = serial.Serial('/dev/ttyUSB3', '115200', timeout=1)
print('Connection is working')

value1 = 0
value2 = 0
value3 = 0
value4 = 0

class App:

    def readdata(self):
        Arduino.write(bytes('n', 'utf-8'))
        for x in range(0, 6):
         globals()['raw%s' % x] = Arduino.readline().decode().strip()
        self.value1 = int(raw1)
        self.value2 = int(raw2)
        self.value3 = int(raw3)
        self.value4 = int(raw4)
        App.changelabels(self.mainframe)

    def changelabels(self):
        label1.config(text=self.value1.get())

    def __init__(self, master=None):
        # build ui
        self.appwindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.appwindow.configure(height=240, width=320)
        self.appwindow.minsize(320, 240)
        self.mainframe = ttk.Frame(self.appwindow)
        self.mainframe.configure(height=240, width=320)
        label1 = ttk.Label(self.mainframe)
        self.value1 = tk.IntVar()
        label1.configure(textvariable=self.value1)
        label1.grid(column=1, row=0)
        label2 = ttk.Label(self.mainframe)
        self.value2 = tk.IntVar()
        label2.configure(textvariable=self.value2)
        label2.grid(column=1, row=1)
        label3 = ttk.Label(self.mainframe)
        self.value3 = tk.IntVar()
        label3.configure(textvariable=self.value3)
        label3.grid(column=1, row=2)
        label4 = ttk.Label(self.mainframe)
        self.value4 = tk.IntVar()
        label4.configure(textvariable=self.value4)
        label4.grid(column=1, row=3)
        self.text1 = ttk.Label(self.mainframe)
        self.text1.configure(text='Value1: ')
        self.text1.grid(column=0, row=0)
        self.text2 = ttk.Label(self.mainframe)
        self.text2.configure(text='Value2: ')
        self.text2.grid(column=0, row=1)
        self.text3 = ttk.Label(self.mainframe)
        self.text3.configure(text='Value3: ')
        self.text3.grid(column=0, row=2)
        self.text4 = ttk.Label(self.mainframe)
        self.text4.configure(text='Value4:  ')
        self.text4.grid(column=0, row=3)
        progressbar1 = ttk.Progressbar(self.mainframe)
        progressbar1.configure(orient="horizontal")
        progressbar1.grid(column=2, row=0)
        progressbar2 = ttk.Progressbar(self.mainframe)
        progressbar2.configure(orient="horizontal")
        progressbar2.grid(column=2, row=1)
        progressbar3 = ttk.Progressbar(self.mainframe)
        progressbar3.configure(orient="horizontal")
        progressbar3.grid(column=2, row=2)
        progressbar4 = ttk.Progressbar(self.mainframe)
        progressbar4.configure(orient="horizontal")
        progressbar4.grid(column=2, row=3)
        self.refresh = ttk.Button(self.mainframe)
        self.refresh.configure(text='Refresh')
        self.refresh.configure(command=self.readdata)
        self.refresh.grid(column=1, row=4)
        self.mainframe.pack(side="top")

        # Main widget
        self.mainwindow = self.appwindow

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()