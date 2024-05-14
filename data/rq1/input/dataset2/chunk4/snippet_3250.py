#Source: https://stackoverflow.com/questions/75181755/function-call-for-pong-game-made-in-python-throwing-attributeerror-error
from gamescreen import GameScreen
from player import Player
import time
from ball import Ball

screen = GameScreen()
screen = screen.screen
player_1 = Player()
player_2 = Player()
player_1.left()
player_2.right()
player_1.show()
player_2.show()
ball = Ball()

screen.onkeypress(fun = player_1.up, key='w')
screen.onkeypress(fun = player_1.down, key='s')
screen.onkeypress(fun = player_2.up, key='Up')
screen.onkeypress(fun = player_2.down, key='Down')

on = True
while on:
    ball.move()

screen.exitonclick()