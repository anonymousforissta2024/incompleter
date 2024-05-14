#Source: https://stackoverflow.com/questions/76171186/i-cant-add-a-widget-in-a-kivy-app-from-python3-class-error-message-attributee
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
class Grid(GridLayout):
    cols=2
    def doet(self):
        self.ids.grid_id.add_widget(Button())
class app(App):
    def build(self):
        self.grid=Grid()
        return Builder.load_file('lab.kv')
app().run()