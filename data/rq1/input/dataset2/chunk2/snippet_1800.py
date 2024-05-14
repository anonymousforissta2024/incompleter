#Source: https://stackoverflow.com/questions/63807388/kivy-scrollview-attributeerror-nonetype-object-has-no-attribute-bind
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.app import runTouchApp
from kivy.uix.button import Button

KV = """
Screen:
    Controller:
        layout_content: layout_content
        BoxLayout:
            id: bl
            orientation: 'vertical'
            padding: 10, 10
            row_default_height: '48dp'
            row_force_default: True
            spacing: 10, 10
            ScrollView:
                size: self.size
                GridLayout:
                    id: layout_content
                    size_hint_y: None
                    cols: 1
                    row_default_height: '20dp'
                    row_force_default: True
                    spacing: 0, 0
                    padding: 0, 0
                    
                    MDCard:
                        id: tel1
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 1"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del primo"
                    MDCard:
                        id: tel2
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 2"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del secondo"
                    MDCard:
                        id: tel2
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 3"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]     
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del terzo" 
                    MDCard:
                        id:tel4
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Telefilm 4"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del quarto"
                    MDCard:
                        id:tel5
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 5"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del quinto"                 
"""

class Controller(FloatLayout):
    layout_content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.layout_content.bind(minimum_height=self.layout_content.setter('height'))

class MainApp(MDApp):
    def build(self):
        self.title = "LukeFlix"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

MainApp().run()