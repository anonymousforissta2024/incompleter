#Source: https://stackoverflow.com/questions/74895052/python-attributeerror-module-core-has-no-attribute-children
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

Builder.load_file("layouts/screen_manager.kv")


class WindowManager(ScreenManager):
    pass