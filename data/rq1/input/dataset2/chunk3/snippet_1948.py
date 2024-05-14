#Source: https://stackoverflow.com/questions/59416972/python-kivy-attributeerror-nonetype-object-has-no-attribute-bind
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty, BooleanProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder 

import calculator_calc




Builder.load_file("calculatorgui.kv")



class CalculatorScreen1(Screen):
    pass

class CalculatorScreen2(Screen):
    pass



class CalculatorModeIndicator(BoxLayout):
    pass

class CalculatorMonitor1(BoxLayout):
    pass

class CalculatorButtons(BoxLayout):
    pass





screen_manager = ScreenManager()

screen_manager.add_widget(CalculatorScreen1(name = "screen1"))
screen_manager.add_widget(CalculatorScreen2(name = "screen2"))



class Calculator(App):
    expression_tokens = ListProperty([])
    expression_value = StringProperty("")
    angle_mode = StringProperty("degrees")
    angle_mode_text = StringProperty("D")
    button_mode = NumericProperty(1)
    button_mode_text = StringProperty("1ST")
    store_mode = BooleanProperty(False)


    def build(self):
        return screen_manager


    def switch_screen(self, screen):
        screen_manager.current = screen

    def set_button_mode(self, button_mode):
        self.button_mode = button_mode

        if button_mode == 1:
            self.button_mode_text = "1ST"
        elif button_mode == 2:
            self.button_mode_text = "2ND"
        elif button_mode == 3:
            self.button_mode_text = "3RD"  

    def set_angle_mode(self, angle_mode):
        calculator_calc.evaluate(f"angle_mode {angle_mode}") 

        self.angle_mode = angle_mode

        if angle_mode == "degrees":
            self.angle_mode_text = "D"
        elif angle_mode == "radians":
            self.angle_mode_text = "R"
        elif angle_mode == "gradians":
            self.angle_mode_text = "G"  

    def add_token(self, token):
        self.expression_tokens.append(token)

    def calculate(self, expression):
        result = calculator_calc.evaluate(expression)
        self.expression_value = str(result)
        calculator_calc.evaluate(f"ANS = {result}")


Calculator().run()