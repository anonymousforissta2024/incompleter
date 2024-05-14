#Source: https://stackoverflow.com/questions/74254584/typeerror-invalid-rect-assignment
import pygame

# normal setup
pygame.init()
screen = pygame.display.set_mode((700, 700), pygame.RESIZABLE)
pygame.display.set_caption('ZAP!')
icon = pygame.image.load('download.jpg')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True  # while loop running so after ending game i can still run

# bg
bg = pygame.image.load('ok_proper.jpg')
bg_pic = pygame.transform.scale(bg, (700, 700))


class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Graphics/yes.png'),(100,100)),90)
        self.rect = self.image.get_rect(topright = (pos))
        self.speed = 10
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect = self.image.get_rect(topright= (pos))




class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Graphics/spaceship.png')
        self.rect = self.image.get_rect(bottomleft=(250, 700))
        self.speed = 5
        self.laser_time = 0
        self.laser_cooldown = 600
        self.ready = True
        self.shoot = pygame.sprite.Group()

    def movement(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right + self.speed < 699:
            self.rect.x += self.speed
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x - self.speed > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_SPACE] and self.ready:
            self.shootlaser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def shootlaser(self):
        if not self.ready:
            timeoflaser = pygame.time.get_ticks()
            if self.laser_time - timeoflaser == self.laser_cooldown:
                self.ready = True
        else:
            self.shoot.add(Bullet(self.rect.topright))



    def update(self):
        self.movement()
        self.shootlaser()

# spaceship
spaceship = Spaceship()
# spaceship = pygame.sprite.GroupSingle()
# spaceship.add(Spaceship())

# bullet
bullet = Bullet(spaceship)

while running:
    clock.tick(60)
    screen.blit(bg_pic, (0, 0))  # background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(spaceship.image,spaceship.rect)
    screen.blit(bullet.image,bullet.rect)
    spaceship.update()
    # spaceship.draw(screen)
    pygame.display.update()