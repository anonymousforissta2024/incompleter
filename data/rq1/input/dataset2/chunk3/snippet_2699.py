#Source: https://stackoverflow.com/questions/64988130/error-typeerror-item-1-in-argtypes-passes-a-union-by-value-which-is-unsuppo
import wx
import wx.lib.activex
import csv
import comtypes.client

class EventSink(object):

    def __init__(self, frame):
        self.counter = 0
        self.frame = frame

    def DataReady(self):
        self.counter +=1
        self.frame.Title= "DataReady fired {0} times".format(self.counter)

class MyApp( wx.App ): 

    def __init__( self, redirect=False, filename=None ):
        wx.App.__init__( self, redirect, filename )
        self.initUI()
        self.bindUI()

    def bindUI(self):
        self.myb1.Bind(wx.EVT_BUTTON, self.myb1click)
        self.myb2.Bind(wx.EVT_BUTTON, self.myb2click)

    def initUI(self):
        self.frame = wx.Frame( parent=None, id=wx.ID_ANY,size=(760,500), title='Python Interface to DataRay')
        #Panel
        p = wx.Panel(self.frame, wx.ID_ANY)
        #Get Data
        self.gd = wx.lib.activex.ActiveXCtrl(p, 'DATARAYOCX.GetDataCtrl.1')
        self.gd.ctrl.StartDriver()#The methods of the object are available through the ctrl property of the item
        sink = EventSink(self.frame)
        self.sink = comtypes.client.GetEvents(self.gd.ctrl, sink)
        #Button Panel
        bp = wx.Panel(parent=self.frame, id=wx.ID_ANY, size=(215, 250))
        b1 = wx.lib.activex.ActiveXCtrl(parent=bp,size=(200,50), pos=(7, 0),axID='DATARAYOCX.ButtonCtrl.1')
        b1.ctrl.ButtonID =297 #Id's for some ActiveX controls must be set
        b2 = wx.lib.activex.ActiveXCtrl(parent=bp,size=(100,25), pos=(5, 55),axID='DATARAYOCX.ButtonCtrl.1')
        b2.ctrl.ButtonID =86
        b3 = wx.lib.activex.ActiveXCtrl(parent=bp,size=(100,25), pos=(110,55),axID='DATARAYOCX.ButtonCtrl.1')
        b3.ctrl.ButtonID =87
        b4 = wx.lib.activex.ActiveXCtrl(parent=bp,size=(100,25), pos=(5, 85),axID='DATARAYOCX.ButtonCtrl.1')
        b4.ctrl.ButtonID =96
        b4 = wx.lib.activex.ActiveXCtrl(parent=bp,size=(100,25), pos=(110, 85),axID='DATARAYOCX.ButtonCtrl.1')
        b4.ctrl.ButtonID =9
        
        #Custom controls
        t = wx.StaticText(bp, label="File:", pos=(5, 115))
        self.ti = wx.TextCtrl(bp, value="C:\\Users\\Public\\Documents\\output.csv", pos=(30, 115), size=(170, -1))
        self.rb = wx.RadioBox(bp, label="Data:", pos=(5, 140), choices=["Profile"])
        self.cb = wx.ComboBox(bp, pos=(5,200), choices=[ "Profile_X", "Profile_Y", "Both"])
        self.cb.SetSelection(0)
        self.myb1 = wx.Button(bp, label="Write", pos=(5,225))
        self.myb2 = wx.Button(bp, label="Switch", pos=(110,225))
        #Pictures
        wanderer = wx.lib.activex.ActiveXCtrl(parent=self.frame,size=(250,250),axID='DATARAYOCX.ButtonCtrl.1')
        wanderer.ctrl.ButtonID = 197
        tpic = wx.lib.activex.ActiveXCtrl(parent=self.frame,size=(250,250), axID='DATARAYOCX.TwoDCtrl.1')
        palette = wx.lib.activex.ActiveXCtrl(parent=self.frame,size=(10,250), axID='DATARAYOCX.PaletteBarCtrl.1')
        #Profiles
        self.px = wx.lib.activex.ActiveXCtrl(parent=self.frame,size=(300,200),axID='DATARAYOCX.ProfilesCtrl.1')
        self.px.ctrl.ProfileID=4
        self.py = wx.lib.activex.ActiveXCtrl(parent=self.frame,size=(300,200),axID='DATARAYOCX.ProfilesCtrl.1')
        self.py.ctrl.ProfileID =5

        #Formatting 
        row1 = wx.BoxSizer(wx.HORIZONTAL)
        row1.Add(item=bp,flag=wx.RIGHT, border=10)
        row1.Add(wanderer)
        row1.Add(item=tpic, flag=wx.LEFT, border=10)
        
        row2 = wx.BoxSizer(wx.HORIZONTAL)
        row2.Add(self.px, 0, wx.RIGHT, 100)# Arguments: item, proportion, flags, border
        row2.Add(self.py)

        col1 = wx.BoxSizer(wx.VERTICAL)
        col1.Add(item=row1, flag=wx.BOTTOM, border=10)
        col1.Add(item=row2, flag=wx.ALIGN_CENTER_HORIZONTAL)
        self.frame.SetSizer(col1)
        self.frame.Show()

    def myb1click(self,e):
        rb_selection = self.rb.GetStringSelection()
        p_selection = self.cb.GetStringSelection()
        if p_selection == "Profile_X":
            data = self.px.ctrl.GetProfileDataAsVariant()
            data = [[x] for x in data]#csv.writerows accepts a list of rows where each row is a list, a list of lists
        elif p_selection == "Profile_Y":
            data = self.py.ctrl.GetProfileDataAsVariant()
            data = [[x] for x in data]
        else:
            datax = self.px.ctrl.GetProfileDataAsVariant()
            datay = self.py.ctrl.GetProfileDataAsVariant()
            data = [list(a) for a in zip(datax,datay)]#Makes a list of lists; X1 with Y1 in a list, X2 with Y2 in a list etc...
        filename = self.ti.Value
        with open(filename, 'wb') as fp:
            w = csv.writer(fp, delimiter=',')
            w.writerows(data)

    def myb2click(self,e):
        if self.gd.ctrl.AlternateDetector == 0:
            self.gd.ctrl.AlternateDetector = 1
        else:
            self.gd.ctrl.AlternateDetector = 0

if __name__ == "__main__":
     app = MyApp()
     app.MainLoop()