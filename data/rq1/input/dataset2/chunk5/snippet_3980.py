#Source: https://stackoverflow.com/questions/56824210/typeerror-nonetype-object-is-not-subscriptable-kivy-package-problem
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE votes (email NOT NULL, password NOT NULL, votes_yes INTEGER, votes_no INTEGER)""")


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        with conn:
            cur.execute("SELECT * FROM votes WHERE email = ? And password = ?, (self.email.text, self.password.text)")
            result = cur.fetchone()
            if result:
                self.reset()
                sm.current = "voting"
            else:
                invalid_login()

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class VotingWindow(Screen):
    email = ObjectProperty()

    def yes_btn(self):
        with conn:
            cur.execute("UPDATE votes set vote_yes = 1 WHERE email = self.email.text")

    def no_btn(self):
        with conn:
            cur.execute("UPDATE votes set vote_no = 1 WHERE email = self.email.text")


class CreateAccountWindow(Screen):
    email = ObjectProperty()
    password = ObjectProperty()

    def create_btn(self):
        with conn:
            results = cur.execute("SELECT * FROM votes WHERE email = ?, (self.email.text,)")
            if results:
                invalid_form()
            else:
                cur.execute("INSERT into votes VALUES(email = ?, password = ?), (self.email.text, self.password.text)")
                self.reset()

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class WindowManager(ScreenManager):
    pass


def invalid_login():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def invalid_form():
    pop = Popup(title='Error',
                  content=Label(text='An account already exists with that email address'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create account"), VotingWindow(name="voting")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()

conn.close()