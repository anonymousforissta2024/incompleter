#Source: https://stackoverflow.com/questions/60126786/nameerror-instance-of-windowmanager-is-not-defined-kivy
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.theming import ThemeManager
import mysql.connector
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton, MDRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout


Window.clearcolor = (1,1,1,1)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database=""
         )

cur = mydb.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS meet")

cur.execute("CREATE TABLE IF NOT EXISTS users (email VARCHAR(255), password VARCHAR(255))")

cur.close()
mydb.close()


class LoginWindow(Screen):
    password = ObjectProperty(None)

    def login(self, email):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="")
        cur = mydb.cursor(buffered=True)
        cur.execute("SELECT * FROM users WHERE email = %s and password = %s", (email, self.password.text))
        result = cur.fetchone()
        mydb.commit()
        cur.close()
        mydb.close()
        if result:
            self.reset()
            sm.current = "information"
        else:
            invalid_login()

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class WindowManager(ScreenManager):
    pass


class MyApp(App):
    theme_cls = ThemeManager()

    def build(self):
        kv = Builder.load_file("kivy.kv")
        sm = WindowManager()

        screens = [LoginWindow(name="login"),
                   Information(name="information")]
        for screen in screens:
            sm.add_widget(screen)

        sm.current = "login"
        return sm


if __name__ == '__main__':
    MyApp().run()