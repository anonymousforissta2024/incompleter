#Source: https://stackoverflow.com/questions/59461791/kivymd-attributeerror-nonetype-object-has-no-attribute-theme-cls
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.theming import ThemeManager
import mysql.connector


Window.clearcolor = (1,1,1,1)


class Information(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("kivy.kv")
sm = WindowManager()

screens = [Information(name="information")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "information"


class MyApp(App):
    theme_cls = ThemeManager()

    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()