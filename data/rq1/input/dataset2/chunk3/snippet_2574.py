#Source: https://stackoverflow.com/questions/62179706/pygame-error-typeerror-argument-1-must-be-pygame-surface-not-list
import math
import random

import pygame

pygame.init()
# Screen (Pixels by Pixels (X and Y (X = right and left Y = up and down)))
screen = pygame.display.set_mode((800, 600))
running = True
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)
# Player Icon/Image
playerimg = pygame.image.load('Player.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    # Blit means Draw
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    # Blit means Draw
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX[i] - bulletX, 2) + (math.pow(enemyY[i] - bulletY, 2))))
    if distance < 27:
        return True
    else:
        return False


background = pygame.image.load('247.jpg')

# Enemy
num_of_enemy = 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('space-invaders.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 450
bulletX_change = 480
bulletY_change = 10
bullet_state = "ready"

score = 0
# Game loop (Put most of code for game in this loop)
while running:
    screen.fill((255, 0, 0))
    # BAckground
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)



        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # RGB (screen.fill) = red green blue
    # 5 = 5 + - 0.1 -> 5 = 5 - 0.1
    # making so nothing can go out of bounds
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collison
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()