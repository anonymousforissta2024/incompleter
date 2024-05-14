#Source: https://stackoverflow.com/questions/43881184/typeerror-init-got-an-unexpected-keyword-argument-no-builder-kivy
class PlayerImage(Image):
    angle = NumericProperty(0)

    def __init__(self):
        super().__init__()


    def on_touch_down(self, touch):
        # self.currentstate = self.states["person.zip/"]
        Animation.cancel_all(self)
        angle = degrees(atan2(touch.y - self.center_y,
                              touch.x - self.center_x))

        Animation(center=touch.pos, angle=angle).start(self)
        # self.currentstate = self.states["personred/rest.png/"]