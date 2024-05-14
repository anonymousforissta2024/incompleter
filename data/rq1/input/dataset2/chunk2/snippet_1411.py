#Source: https://stackoverflow.com/questions/52066118/i-keep-getting-the-error-typeerror-integer-argument-expected-got-float-in-pyt
import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
sky_blue = (0,150,225)
green = (0,255,0)

displayWidth = 800

displayHeight = 600
#Final :- pygame.display.set_mode((1365, 1050))
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Super Mario')
clock = pygame.time.Clock()

crashed = False

timeOut = False

Quit = False

#50,75
marioStanding = pygame.image.load('Super_Mario_Standing.jpg')
marioStanding = pygame.transform.scale(marioStanding, (displayWidth/40,displayHeight/8))

def Stand(x,y):
    gameDisplay.blit(marioStanding,(x,y))

x = (displayWidth * 0.45)
y = (displayHeight * 0.8)

while not crashed and not timeOut and not Quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit = True

    print (event)

    gameDisplay.fill(sky_blue)
    Stand(x,y)

    pygame.display.update()
    clock.tick(24)

pygame.quit()
quit()