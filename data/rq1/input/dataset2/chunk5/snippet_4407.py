#Source: https://stackoverflow.com/questions/26673926/attributeerror-object-has-no-attribute-velx
import pygame,sys
from classes import *

pygame.init()
WIDTH,HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
img_pokemon = pygame.image.load("pokemon.png")

#colours
clr1 = (22,122,211)
clr2 = (0,44,166)
clr3 = (34,55,245)
clrvar = 1
spritemovex = 1
spritemovey = 1

#clock
clock = pygame.time.Clock()
FPS = 24
fivesecondinterval = FPS * 5
totalframes = 0

pokemon = Pokemon(0, 100, 40, 30, "pokemon.png")

while True:
    #processes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    clock.tick(FPS)

    #logic
    pokemon.motion()

    totalframes += 1
    clrvar +=3
    if clrvar > 255:
        clrvar = 1

    spritemovex += 2
    spritemovey += 2
    if spritemovex > WIDTH:
        spritemovex %= WIDTH
    if spritemovey > HEIGHT:
        spritemovey %= HEIGHT
    #draw
    screen.fill( (90,clrvar,180) )
    screen.blit(img_pokemon, (spritemovex,spritemovey))