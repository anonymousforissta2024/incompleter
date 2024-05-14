#Source: https://stackoverflow.com/questions/71072210/space-invaders-game-strange-typeerror-int-object-is-not-subscriptable-error-i
import pygame
import random
import math
#pygame.time.Clock(30)

# Initialize the game
pygame.init()
# Screen
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('background.png')

# Title and icon
pygame.display.set_caption("Space Invaders")

# player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 510
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(40, 100))
    enemyX_change.append(2)
    enemyY_change.append(40)

# missile
missileImg = pygame.image.load('missile.png')
missileX = playerX
missileY = 483
missileY_change = 6
missile_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, missileX, missileY):
    distance = math.sqrt((math.pow(enemyX - missileX, 2)) + (math.pow(enemyY - missileY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (-100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check what key it is
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -3
            if event.key == pygame.K_d:
                playerX_change = +3
            if event.key == pygame.K_SPACE:
                if missile_state == "ready":
                    missileX = playerX
                    missileY = playerY - 27
                    fire_missile(missileX, missileY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # spaceship boundary
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 740:
        playerX = 740
    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        collision = is_collision(enemyX[i], enemyY[i], missileX, missileY)
        if collision:
            missileY = 483
            missile_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(40, 100)

        enemy(enemyX[i], enemyY[i], i)

    # missile movement
    if missileY < -10:
        missileY = 483
        missile_state = "ready"
    if missile_state is "fire":
        fire_missile(missileX, missileY)
        missileY -= missileY_change
    
    collision = is_collision(enemyX[i], enemyY[i], missileX, missileY)
    if collision:
        missileY = 483
        missile_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(40, 100)

    player(playerX, playerY)
    pygame.display.update()