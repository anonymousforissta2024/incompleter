#Source: https://stackoverflow.com/questions/61030988/pygame-attributeerror-pygame-surface-object-has-no-attribute-display
import pygame, sys, os 
from pygame.locals import *
red = (255,0,0)
pygame.init()
window = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Slither.eat - The Snake Game')
screen = pygame.display.get_surface()
screen.fill(red)
screen.display.set_caption("Snake")
pygame.display.flip()
while True:
    print("Slither.eat - The Snake Game!")
    pass