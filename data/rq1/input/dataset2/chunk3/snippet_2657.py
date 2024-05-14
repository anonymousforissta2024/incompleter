#Source: https://stackoverflow.com/questions/64229421/attributeerror-super-object-has-no-attribute-getattr-in-python
class UserHomeScrren(BoxLayout):
    

    def __init__(self, **kwargs):
        super(UserHomeScrren, self).__init__(**kwargs)
     

    def calculate(self):
        #weight =int(self.weight.text)
        weight=int(self.ids.backdrop.ids.backlayer.bmi_screen.weight.text)
        height= int (self.ids.backdrop.ids.backlayer.bmi_screen.height.text)
        print(self.ids.backlayer.ids.bmi_screen.ids.height)
        BMI = round((weight * 703) / (height ** 2))

        if BMI < 18.5:
            self.ids.results.text += "Your BMI is " + str(BMI) + " which means you are underweight."


    def clear(self):
        self.ids.results.text = ""
        self.ids.weight.text = ""
        self.ids.height.text = ""
        

        print(weight)
        print('calculate.....')


class ItemBackdropBackLayer(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)


class UserApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "User Flana"
        self.theme_cls.primary_palette = "DeepPurple"
        super().__init__(**kwargs)
        Window.size = (300, 550)

    def __getattr__(self, attr):
        return super().__getattr__(attr)

    def build(self):
        return UserHomeScrren()

    
if __name__ == "__main__":
    UserApp().run()