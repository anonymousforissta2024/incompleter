#Source: https://stackoverflow.com/questions/59475230/attributeerror-module-pygame-event-has-no-attribute-type
import pygame
from pygame import *
pygame.init()
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')
game_running = True
while game_running:
    for events in pygame.event.get():
        if event.type == QUIT:
            game_running = False

    display.update()
pygame.quit()