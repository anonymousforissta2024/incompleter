#Source: https://stackoverflow.com/questions/71549880/panda3d-simplepbr-running-problemfilenotfounderror-errno-2-no-such-file-or-d
import sys

import simplepbr
from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        simplepbr.init()

        self.accept('escape', sys.exit)

        # base.disableMouse()

        self.jack = self.loader.loadModel("jack")
        self.jack.reparentTo(self.render)
        self.jack.setScale(2.0, 2.0, 2.0)
        self.jack.setPos(8, 50, 0)



if __name__ == '__main__':
    app = MyApp()
    app.run()