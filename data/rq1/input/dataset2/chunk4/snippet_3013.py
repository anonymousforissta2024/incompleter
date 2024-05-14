#Source: https://stackoverflow.com/questions/75189625/attributeerror-str-object-has-no-attribute-type-in-snake-game
from turtle import Turtle
from random import randint, choice
from foods import foods, shape_names


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(choice(shape_names))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.refresh()

    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.shape(choice(shape_names))
        self.goto(x=rand_x, y=rand_y)