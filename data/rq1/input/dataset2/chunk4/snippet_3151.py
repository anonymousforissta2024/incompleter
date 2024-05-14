#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
import pygame

#screen settings
WIDTH = 1000
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AutoPilot")
screen.fill((255, 255, 255))

#load bullets
bullets = pygame.image.load('car/bullet.png').convert_alpha()

#groups
bullet_group = pygame.sprite.Group()

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, scale, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        #self.x = x
        #self.y = y
        self.moving = True
        self.frame = 0
        self.flip = False
        self.direction = 0

        #load car
        self.images = []
        img = pygame.image.load('car/car.png').convert_alpha()
        img = pygame.transform.scale(img, (int(img.get_width()) * scale, (int(img.get_height()) * scale)))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.update_time = pygame.time.get_ticks()
        self.movingLeft = False
        self.movingRight = False
        self.rect.x = 465
        self.rect.y = 325

    #draw car to screen
    def draw(self):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))

    #move car
    def move(self):
        #reset the movement variables
        dx = 0
        dy = 0

        #moving variables
        if self.movingLeft and self.rect.x > 33:
            dx -= self.speed
            self.flip = True
            self.direction = -1
        if self.movingRight and self.rect.x < 900:
            dx += self.speed
            self.flip = False
            self.direction = 1

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    #shoot
    def shoot(self):
        bullet = bullets.Bullet(self.rect.centerx + 18, self.rect.y + 30, self.direction)
        bullet_group.add(bullet)