#Source: https://stackoverflow.com/questions/26673926/attributeerror-object-has-no-attribute-velx
import pygame

class BaseClass(pygame.sprite.Sprite):

    allsprites = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):

        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height



class Pokemon(BaseClass):
    List = pygame.sprite.Group()
    def __init___(self, x, y, width, height, image_string):

        BaseClass.__init__(self, x, y, width, height, image_string)
        Pokemon.List.add(self)
        self.velx = 3

    def motion(self):

        self.rect.x += self.velx