#Source: https://stackoverflow.com/questions/70048468/python-filenotfounderror-even-if-the-file-is-there
import os
from pyglet import font
font.add_file(str(os.getcwd())+"\\fonts\\Roboto Bold.ttf")