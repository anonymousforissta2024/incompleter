#Source: https://stackoverflow.com/questions/76785114/getting-kivy-attribute-error-super-object-has-no-attribute-getattr-pyth
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.uix.image import Image
import random
import os
from kivy.core.window import Window
import numpy as np
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
imp = "x"
user_inp = "x"


class MyLayout(Widget):
    #THIS IS WHERE THE ERROR SEEMS TO OCCUR
    def correct(self):

        self.ids.text_label.text = "Correct"
        return RootLayout()
    def incorrect(self):
        self.ids.text_label.text = "Incorrect"
        return RootLayout()
        

class RootLayout(FloatLayout):
    pass

prior = StringProperty()

class colorApp(App, FloatLayout):

    flagfile = StringProperty("0")
    
    path = "/Users/sam/Downloads/App/w320"
    files = os.listdir(path)
    #self.important = random.choice(files)
    important = "bt.png"
    flagfile= path + "/" + important
    
    other_answer = StringProperty()
  
    prior = StringProperty()
    def button_press(self):
        #[Removed Code]
 
        print(self.correct_answer)
        self.imp = self.correct_answer
        
        self.prior = self.root.ids.user_input.text.lower()

        user_inp = self.prior

        #THIS IS WHERE I CALL THE FUNCTION <------
        if user_inp == self.imp:   
            MyLayout().correct()
        else:
            MyLayout().incorrect()
        
        print(self.prior)
        print(self.imp)
        print(self.important)
        print(user_inp)

        return RootLayout()

    def build(self):
        return RootLayout()

    
if __name__ == "__main__":
    colorApp().run()