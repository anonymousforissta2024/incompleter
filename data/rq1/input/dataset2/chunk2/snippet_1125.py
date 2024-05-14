#Source: https://stackoverflow.com/questions/37057027/attributeerror-pygame-surface-object-has-no-attribute-add-internal
import pygame, sys, os
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((100, 100))

tile_l1_list = pygame.sprite.Group()

image = pygame.image.load("box.png")
image = image.convert_alpha()
a=screen.blit(image, (10,10))
pygame.display.flip()
tile_l1_list.add(image)


####################################

while True:
    pygame.display.flip()

pygame.quit()