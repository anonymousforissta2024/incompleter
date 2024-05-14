#Source: https://stackoverflow.com/questions/68157511/typeerror-when-drawing-circle-in-pygame
import pygame
from circle import Circle
from draw import Draw
from Box2D import b2World

PPM = 20
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS

pygame.init()
screen = pygame.display.set_mode((600, 480))
clock = pygame.time.Clock()

# A list for all of our rectangles
world = b2World(gravity=(0, 30), doSleep=True)


close = False

while not close:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
    
    screen.fill((255,255,255))
    
    circle = Circle(world,300,300,PPM)
    
    Draw(screen,world.bodies,PPM)
    
    world.Step(TIME_STEP, 10, 10)
    pygame.display.flip()
    clock.tick(TARGET_FPS)

pygame.quit()