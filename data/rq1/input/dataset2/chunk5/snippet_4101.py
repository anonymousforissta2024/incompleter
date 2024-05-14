#Source: https://stackoverflow.com/questions/59201728/having-a-problem-with-the-kivy-attribute-error-how-to-fix-attributeerror-none
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.theming import ThemeManager
from kivymd.uix.menu import MDDropdownMenu
from kivy.factory import Factory

from kivy.lang import Builder
Builder.load_file('user/user.kv')

class MyTab(BoxLayout, MDTabsBase):
    pass


class MyTab2(BoxLayout, MDTabsBase):
    pass


class MyTab3(BoxLayout, MDTabsBase):
    pass


class UserWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UserApp(MDApp):

    title = 'DEMO'
    dropdown = ObjectProperty()

    def __init__(self, **kwargs):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Gray"
        super().__init__(**kwargs)

    def on_start(self):
        # Create the dropdown menu
        self.dropdown = MDDropdownMenu(width_mult=2)

        # Add items to the menu
        for i in range(6):
            self.dropdown.items.append(
                {"viewclass": "MDMenuItem",
                 "text": "Option " + str(i),
                 "callback": self.option_callback}
            )

    def option_callback(self, text_of_the_option):
        print(text_of_the_option)

    def build(self):
        screen = Factory.UserWindow()

        tab = MyTab(text='Home Tab')
        screen.ids.android_tabs.add_widget(tab)

        tab = MyTab2(text='Approved Tickets')
        screen.ids.android_tabs.add_widget(tab)

        tab = MyTab3(text='History')
        screen.ids.android_tabs.add_widget(tab)
        return screen


if __name__ == '__main__':
    oa = UserApp()
    oa.run()