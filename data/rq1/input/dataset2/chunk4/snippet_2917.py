#Source: https://stackoverflow.com/questions/41909280/gamedisplay-fillwhite-nameerror-name-white-is-not-defined
import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ninja Game')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)    # here
    car(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()