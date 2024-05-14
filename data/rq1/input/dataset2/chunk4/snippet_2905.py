#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
import pygame

#screen settings
WIDTH = 1000
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AutoPilot")
screen.fill((255, 255, 255))

#debris class
class Debris(pygame.sprite.Sprite):
    def __init__(self, scale, speed):
        pygame.sprite.Sprite.__init__(self)

        self.x = 400
        self.y = HEIGHT / 2 - 200
        self.speed = speed
        self.vy = 0
        self.on_ground = True
        self.move = True
        self.health = 100
        self.max_health = self.health
        self.alive = True

        #load debris
        self.images = []
        img = pygame.image.load('debris/cement.png').convert_alpha()
        img = pygame.transform.scale(img, (int(img.get_width()) * scale, (int(img.get_height()) * scale)))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    #draw debris to screen
    def draw(self):
        screen.blit(self.image,(self.x,self.y))