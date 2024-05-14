#Source: https://stackoverflow.com/questions/56587543/trying-to-use-a-class-but-get-a-nonetype-error-with-kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty #Want my ship to be an object (right?)
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition #For menu system
from kivy.lang import Builder



#The different screens
class MainScreen(Screen):
    pass
class SpaceGame(Screen):
    pass
class Installningar(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass


# The game
class SpaceShip(Widget): #The ship is a class
    pass


class SpaceGame_TheGame(Widget):
    player = ObjectProperty(None) #I want the ship to be an object that can get hit and stuff

    def on_touch_move(self,touch): #For movement
       pass
       self.player.center_x = touch.x
       self.player.center_y = touch.y


#Start up stuff
presentation = Builder.load_file("space.kv") #Presentation är bara ett namn på detta som han valde
class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()