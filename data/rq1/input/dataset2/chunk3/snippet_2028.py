#Source: https://stackoverflow.com/questions/63306805/kivy-android-attributeerror-nonetype-object-has-no-attribute-play
import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.core.audio import SoundLoader

class HelloApp(App):
    def build(self):
        self.sound = SoundLoader.load('back.mp3') # open the background music
        self.sound.play() # play the sound
        return Label(text='>>>>>')
if __name__=="__main__":
    HelloApp().run()