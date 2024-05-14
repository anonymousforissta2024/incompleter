#Source: https://stackoverflow.com/questions/59637293/attributeerror-float-object-has-no-attribute-texty
import psutil
import time
import threading
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ExampleApp(App):
    def build(self):
        b = BoxLayout()
        self.texty = Label(text=str(psutil.cpu_percent()))
        b.add_widget(self.texty)
        return b

    def update(self):
            self.texty.text = str(psutil.cpu_percent())

    Clock.schedule_interval(update, 1.0)

ExampleApp().run()