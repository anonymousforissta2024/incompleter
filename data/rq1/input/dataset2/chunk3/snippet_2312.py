#Source: https://stackoverflow.com/questions/54144305/type-error-missing-required-positional-arguments-with-multiple-py-files
from gui_backup import Display
class Baustein:
    x1, y1, x2, y2 = 10,10,20,20
    color = "red"
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color
    def show_new_object(self):
        quadrat2 = Display.create_rectangle(40, 50, 60, 70, fill = color)
        Display.coords(quadrat2, x1, y1, x2, y2)