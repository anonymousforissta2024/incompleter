#Source: https://stackoverflow.com/questions/63642052/kivy-typeerror-nonetype-object-is-not-callable-for-mainapp-run
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('main.kv')


class DigitalLove(App):
    @property
    def build(self):

        return GUI

        monika_art = 'images/monika.png'
        textbox_img = 'images/textbox.png'

        doki_response = 'example text'


if __name__ == "__main__":
    DigitalLove().run()