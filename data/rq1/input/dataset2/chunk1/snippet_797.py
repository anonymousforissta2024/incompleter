#Source: https://stackoverflow.com/questions/54404044/typeerror-argument-1-must-be-pygame-surface-not-pygame-rect-in-my-python-game
# Imports--------------------------------------------------------------------------------------------------------------#

import pygame


# initialization-------------------------------------------------------------------------------------------------------#

pygame.init()

# Flags----------------------------------------------------------------------------------------------------------------#

gameExit = False

# Variables -----------------------------------------------------------------------------------------------------------#

display_height = 500
display_width = 500
bg = (0, 0, 0)
isJump = False
# Colors --------------------------------------------------------------------------------------------------------------#

FUCHSIA = (255, 0, 255)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
AQUA = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Draw Screen----------------------------------------------------------------------------------------------------------#

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Airbender Training")
Clock = pygame.time.Clock()

# Mobs ----------------------------------------------------------------------------------------------------------------#
class entity:
    #Entities will be every mob in the game
    def __init__(self, width, height, velocity, x, y, sprite):

        entity.width = width
        entity.height = height
        entity.velocity = velocity
        entity.x_position = x
        entity.y_position = y
        entity.sprite = sprite

player_width = 64
player_height = 64
player_velocity = 5
player_x_position = 5
player_y_position = 5
player_sprite = pygame.draw.rect(win, RED, (player_x_position, player_y_position, player_width, player_height))
    # ^This makes a placeholder red square^
player = entity(player_width, player_height, player_velocity, player_x_position, player_y_position, player_sprite)

# Functions -----------------------------------------------------------------------------------------------------------#

def drawGameWindow():

    win.fill(bg)
    win.blit(player_sprite, player.x_position, player.y_position)
    Clock.tick(60)
    pygame.display.update()

def jump():

    jumpCount = 1
    while jumpCount <= entity.height * 1.5:
        entity.y_position += jumpCount
        jumpCount += 1
    while jumpCount >= entity.height * 1.5:
        entity.y_position -= jumpCount
        jumpCount -= 1

# Main Loop------------------------------------------------------------------------------------------------------------#

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event == pygame.k_RIGHT or event == pygame.k_D:
                player.x_position += 5
            if event == pygame.k_LEFT or event == pygame.k_A:
                player.x_position -= 5
            while not isJump:
                if event == pygame.k_up or event == pygame.k_SPACE:
                    jump(player)

    drawGameWindow()

pygame.quit()