#Source: https://stackoverflow.com/questions/50412552/kivy-callback-custom-widget-call-from-ids-raise-attributeerror
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("panel.kv")

class LabelBox(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(LabelBox, self).__init__(*args, **kwargs)

    def change_first_text(self, text):
        self.ids.first.text = text

class ButtonList(BoxLayout):
    pass

class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        self.test = Test()
        self.btn_list = ButtonList()
        self.vbox = BoxLayout(orientation="vertical")
        self.vbox.add_widget(self.btn_list)
        self.vbox.add_widget(self.test)
        return self.vbox

    def change_first(self, value):
        print("Button clicked and new value is: '{}'".format(value))
        self.test.ids.lbs.change_first_text(value)


if __name__ == '__main__':
    TabbedPanelApp().run()