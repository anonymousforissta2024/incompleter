#Source: https://stackoverflow.com/questions/58469331/kivy-attributeerror-with-property-defined-in-kv-file
# File name: drawingspace.py
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout


class DrawingSpace(RelativeLayout):
    def on_children(self, instance, value):
        self.status_bar.counter = len(self.children)  # Here the error states that
                                                      # status_bar attr does not exist