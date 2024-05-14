#Source: https://stackoverflow.com/questions/43940194/kivy-typeerror-on-keyboard-down-takes-2-positional-arguments-but-5-were-given
class PlayerImage(Image):
    angle = NumericProperty(0)

    def __init__(self,**kwargs):
        super(PlayerImage, self).__init__(**kwargs)
        self.states = {"personred/rest.png/": 0,
                       "person.zip/": 1}
        self.currentstate = self.states["personred/rest.png/"]

        self.art = "./rpgArt/" + str(self.currentstate)
        self._keyboard = Window.request_keyboard(self,None)
        if not self._keyboard:
            return
        self._keyboard.bind(on_key_down=self.on_keyboard_down)


    def on_keyboard_down(self, keycode): # KEYBOARD FUNC
        if keycode[1] == "right": 
            self.x += 10
        if keycode[1] == "left":
            self.x -= 10


    def on_touch_down(self, touch):
        self.currentstate = self.states["person.zip/"]
        Animation.cancel_all(self)
        angle = degrees(atan2(touch.y - self.center_y,
                              touch.x - self.center_x))

        Animation(center=touch.pos, angle=angle).start(self)
        self.currentstate = self.states["personred/rest.png/"]