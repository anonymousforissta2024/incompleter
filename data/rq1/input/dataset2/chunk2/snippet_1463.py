#Source: https://stackoverflow.com/questions/67712782/using-pypubsub-wxpython-to-transfer-data-between-windows-getting-typeerror
from pubsub import pub
import wx

class MainFrame (wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title = title, size = (200,200))
        self.panel = MainPanel(self)

class CoordFrame (wx.Frame):
    def __init__(self, parent, title):
        super(CoordFrame, self).__init__(parent, title = title, size = (200,200))
        self.panel = CoordPanel(self)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        vsizer = wx.BoxSizer(wx.VERTICAL)
    
        self.tbxNewMap = wx.TextCtrl(self, id=1001, pos=(20,20), size = (50,20) ,style = wx.TE_CENTER|wx.TE_NOHIDESEL|wx.TE_PROCESS_ENTER)
        vsizer.Add(self.tbxNewMap)

        self.btnEnterNewMap = wx.Button(self, id=1002, label = "New Data", pos = (20,80), size = (80,40))
        vsizer.Add(self.btnEnterNewMap,0,wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.onButtonNewMap, id=1002)

    def onButtonNewMap(self,event):
        temp = self.tbxNewMap.GetValue()
        pub.sendMessage("coord_listener", temp)
        coordframe = CoordFrame(None,"Entry")
        coordframe.Show()

class CoordPanel(wx.Panel):
    def __init__(self, parent):
        super(CoordPanel, self).__init__(parent)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        pub.subscribe(self.coord_listener, "coord_listener")

        self.tbxNewMapNumber = wx.TextCtrl(self, id=1000, pos=(20,20), size = (50,20), style = wx.TE_CENTER|wx.TE_NOHIDESEL|wx.TE_PROCESS_ENTER)
        vsizer.Add(self.tbxNewMapNumber)
        
    def coord_listener(self, message):
        newmapnum = message
        self.tbxNewMapNumber.SetValue(newmapnum)
        self.tbxNewMapNumber.Refresh()


class GMDash(wx.App):
    def OnInit(self):
        self.mainframe = MainFrame(parent = None, title = "Dashboard")
        self.mainframe.Show()
        return True

app = GMDash()
app.MainLoop()