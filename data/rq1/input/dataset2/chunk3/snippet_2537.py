#Source: https://stackoverflow.com/questions/70082191/pygame-not-blitting-image-instead-spitting-out-type-error
import pygame

#Initialize pygame module
pygame.init()

#Create Screen
screen = pygame.display.set_mode((1000, 600))

#Title and Icon
pygame.display.set_caption("Jungle Invader")
icon = pygame.image.load('fox-sitting.png')
pygame.display.set_icon(icon)

# Player
player = pygame.image.load('cat.png')
playerX = 300
playerY = 500

def player():
    screen.blit(player, (playerX, playerY))


#Main loop
running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((244, 232, 255))
    player()