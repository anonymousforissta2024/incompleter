#Source: https://stackoverflow.com/questions/44275919/kivy-attributeerror-nonetype-object-has-no-attribute-bind-when-accessing-l
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from snartoolsmod import *

Builder.load_file("snartools.kv")

class DiningButton(Button):
    pass

class DirectionButton(Button):
    pass

class ItemButton(Button):
    pass

class SubmenuButton(Button):
    pass

class HomeScreen(Screen):
    pass

class WhitmansMenu(Screen):

    def initialize_list(self):
        itemList = Menu('whitmans')
        global allItems
        allItems = itemList.getCopy()
        return itemList

    def modify_list(self, itemList, value, dish):
        if value == 'down':
            for item in itemList:
                if dish == item.getDish():
                    itemList.remove(item)
                    break
        else:
            for item in allItems:
                if dish == item.getDish():
                    itemList.append(item)
                    break

    def modify_state(self, value, submenu, length):
        if value == 'down':
            for i in range(1, length+1):
                button = self.ids[str(submenu)+'_item'+str(i)]
                button.state = 'down'
        else:
            for i in range(1, length+1):
                button = self.ids[str(submenu)+'_item'+str(i)]
                button.state = 'normal'

class ToolScreen(Screen):
    pass

class ToolButton(Button):
    pass

class InstructionsLabel(Label):
    pass

class SubLabel(Label):
    pass

class LengthExact(Screen):

    def get_list(self, itemList):
        return itemList

class LengthRange(Screen):
    pass

class PriceExact(Screen):
    pass

class PriceRange(Screen):
    pass

class MoreExact(Screen):
    pass

class MoreRange(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(HomeScreen(name="home_screen"))
screen_manager.add_widget(WhitmansMenu(name="whitmans_menu"))
screen_manager.add_widget(ToolScreen(name="tool_screen"))
screen_manager.add_widget(LengthExact(name="length_exact"))
screen_manager.add_widget(LengthRange(name="length_range"))
screen_manager.add_widget(PriceExact(name="price_exact"))
screen_manager.add_widget(PriceRange(name="price_range"))
screen_manager.add_widget(MoreExact(name="more_exact"))
screen_manager.add_widget(MoreRange(name="more_range"))

class SnartoolsApp(App):

    def build(self):
        return screen_manager

app = SnartoolsApp()
app.run()