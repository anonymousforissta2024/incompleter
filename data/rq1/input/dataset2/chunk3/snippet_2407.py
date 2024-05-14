#Source: https://stackoverflow.com/questions/62918598/how-to-solve-attributeerror-in-kivy-python
from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_string("login.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyMainApp().run()