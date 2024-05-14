#Source: https://stackoverflow.com/questions/59201728/having-a-problem-with-the-kivy-attribute-error-how-to-fix-attributeerror-none
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager

from kivy.lang import Builder
Builder.load_file('signin/sign.kv')

class LoginScreen(BoxLayout):

    def validate_user(self):
        user = self.ids.email_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw =='':
            info.text = '[color=#FF0000]username and/ or password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Logged In Succesfully!![/color]'
            else:
                info.text = '[color=#FF0000]Invalid Username and/ or Password[/color]'

class SignApp(MDApp):
    title = "LOGIN SCREEN"

    def build(self):
        return LoginScreen()



    def show_password(self, field, button):
        """
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        """

        # Show or hide text of password, set focus field
        # and set icon of right button.
        field.password = not field.password
        field.focus = True
        button.icon = 'eye' if button.icon == 'eye-off' else 'eye-off'


if __name__ == '__main__':
    sa = SignApp()
    sa.run()