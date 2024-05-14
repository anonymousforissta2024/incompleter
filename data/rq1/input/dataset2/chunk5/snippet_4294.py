#Source: https://stackoverflow.com/questions/60388935/trying-my-best-to-understand-this-attributeerror-nonetype-object-has-no-attr
import kivymd
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.properties import ObjectProperty


class MainApp(MDApp):

    height_feet = ObjectProperty(None)
    height_feet = height_feet
    height_inches = ObjectProperty(None)
    weight = ObjectProperty(None)
    bmiout = ObjectProperty(None)


    def calculate(self):
        height_feet = float(self.height_feet.text)
        height_feet = float(height_feet * 12)
        height_inches = float(self.height_inches.text)
        height = float(height_feet + height_inches)
        weight = float(self.weight.text)
        bmi = int(weight / (height * height) * 703)
        percent = str("%")
        self.bmiout.text = "{}{}".format(bmi, percent)
        self.height_feet.text = ""
        self.height_inches.text = ""
        self.weight.text = ""


    def __init__(self, **kwargs):
        self.title = "BMI"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)



MainApp().run()