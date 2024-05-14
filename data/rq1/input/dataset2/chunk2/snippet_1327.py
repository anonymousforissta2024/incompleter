#Source: https://stackoverflow.com/questions/64795214/why-am-i-getting-nameerror-wolf-is-not-defined
import pygame
import random
import Colors

    
class Wolf(pygame.sprite.Sprite):    
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.rect = self.image.get_rect()