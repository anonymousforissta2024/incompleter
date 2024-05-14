#Source: https://stackoverflow.com/questions/69802113/typeerror-init-takes-3-positional-arguments-but-4-were-given-keyboard-com
import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Player(Block):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(200, 20,20)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list.add(block)


player = Player(RED, 20, 20)
all_sprites_list.add(player)


done = False

clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect_x = player.change_x

    screen.fill(WHITE)

    pos = pygame.mouse.get_pos()

    player.rect.x = player.rect.x
    player.rect.y = player.rect.y


    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)


    for block in blocks_hit_list:
        score += 1
        print(score)


    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()