#Source: https://stackoverflow.com/questions/69716472/how-do-i-solve-the-attribute-error-in-kivy
from kivy.uix.widget import Widget
class widget_example(GridLayout):
    def button_click(self):
        print('button clicked')  
class MainWidget(Widget):
    pass
class thelabapp(App):
    pass

if __name__ == '__main__':
    thelabapp().run()