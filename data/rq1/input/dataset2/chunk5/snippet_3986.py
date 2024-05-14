#Source: https://stackoverflow.com/questions/62208703/in-wxgrid-with-two-sizers-when-i-try-to-add-event-receive-this-error-typeerro
import wx
import wx.grid
from wx.lib.scrolledpanel import ScrolledPanel


class TestPanel(ScrolledPanel):
    def __init__(self, parent):
        ScrolledPanel.__init__(self, parent, wx.ID_ANY, size=(640, 480))
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self._create_table(), 1, wx.EXPAND | wx.ALL, 5)

        vbox1 = wx.FlexGridSizer ( rows = 1 , cols = 3 , hgap = 5 , vgap = 5 ) #rows = 3 , cols = 1
        self.b1 = wx.Button(self, -1, "Button 1")
        self.b2 = wx.Button(self, -1, "Button 2")
        self.b3 = wx.Button(self, -1, "Button 3")

        button_sizer = wx.BoxSizer(wx.VERTICAL) # HORIZONTAL
        button_sizer.Add(self.b1)
        button_sizer.Add(self.b2)
        button_sizer.Add(self.b3)
        vbox1.Add ( button_sizer )

        vbox1.Add ( self.sizer )

        midPan1 = wx.Panel ( self )
        midPan1.SetBackgroundColour ( '#ededed' )

        vbox1.Add ( midPan1 , wx.ID_ANY , wx.EXPAND | wx.ALL , 20 )

        self.SetSizer ( vbox1 )


        self.SetupScrolling()
        self.SetAutoLayout(1)

        self.b1.Bind ( wx.EVT_BUTTON , self.be1 )

    def be1 (self) :
        print ( "7654321" )


    def _create_table(self):
        _table = wx.grid.Grid(self, -1)
        _table.CreateGrid(0, 10)
        for i in range(30):  # Work normally If I use 1722 rows
            _table.AppendRows()
            _table.SetCellValue(i, 0, str(i))
        return _table

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                title="Scroll table", size=(640, 480))
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        self.fSizer.Add(TestPanel(self), 1, wx.EXPAND)
        self.SetSizer(self.fSizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = TestFrame()
    app.MainLoop()