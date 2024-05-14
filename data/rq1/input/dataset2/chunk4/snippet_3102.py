#Source: https://stackoverflow.com/questions/75181755/function-call-for-pong-game-made-in-python-throwing-attributeerror-error
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle(shape="circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.setheading(random.randint(1, 360))

    def collide(self):
        current_heading = self.ball.heading()
        self.ball.setheading(180 - current_heading)

    def wall(self):
        if self.ball.ycor() == 350 or self.ball.ycor() == -350:
            self.ball.collide()
        else:
            pass

    def move(self):
        self.ball.forward(5)
        self.ball.wall()