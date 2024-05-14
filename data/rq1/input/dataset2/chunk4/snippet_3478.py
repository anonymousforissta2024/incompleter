#Source: https://stackoverflow.com/questions/45065390/error-attributeerror-module-pygame-has-no-attribute-colors
#Snake Game!
#Our game imports
import pygame
import sys
import random
import time

check_errors = pygame.init()

#(6,0)

if check_errors[1] > 0:
    print("(!) Had {0} initializing error, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame sucessfully initialized")

# Play surface. Create a black surface for game


playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("SNAKE GAME")
time.sleep(5)

#Colors - r,g,b -- red green blue

red = pygame.Colors(255,0,0) #gameover
green = pygame.Colors(0,255,0) #snake
#black
black = pygame.Colors(0,0,0) #score
white = pygame.Colors(255,255,255) #background
brown = pygame.Colors(165,42,42) #food

# FPS frames per seconds controller 
fpsController = pygame.time.Clock()

#where do you want the snake to start
#Important variables

snakePos = [100,50] #should be less than the screen size - (720,460)
snakeBoday =  [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

#Game over function

def gameOver():
    myFont = pygame.font.SysFont('monaco',72)
    GOsurf = myFont.render('Game Over!!', True, red)
    GOrect = Gosurf.get_rect()
    Gorect.midtop = (360, 15)
    playSurface.blit(GOsurf,GOrect)
    python.display.flip()

gameOver()
time.sleep(10)