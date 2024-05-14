#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
import pygame
from autopilot import debris, bullet_group

#screen settings
WIDTH = 1000
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AutoPilot")
screen.fill((255, 255, 255))

#load bullets
bullets = pygame.image.load('car/bullet.png').convert_alpha()

#bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.speed = 5
        self.image = bullets
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

    def update(self):
        self.rect.centery -= self.speed
        #check if bullet has gone off screen
        if self.rect.top < 1:
            self.kill()
        #check collision with cement block
        if pygame.sprite.spritecollide(debris, bullet_group, False):
            if debris.alive:
                debris.health -= 25