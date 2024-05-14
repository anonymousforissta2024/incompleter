#Source: https://stackoverflow.com/questions/61684725/getting-typeerror-object-init-takes-no-parameters-kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ClinicBanner(GridLayout):
    rows = 1

    def __init__(self, **kwargs):
        super(ClinicBanner, self).__init__(**kwargs)

        centre = FloatLayout()
        centre_label = Label(text=kwargs['cities'], size_hint=(1, .2), pos_hint={"top": .2,  "left": 1})
        centre.add_widget(centre_label)

        self.add_widget(centre)