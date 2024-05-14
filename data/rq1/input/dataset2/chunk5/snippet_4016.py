#Source: https://stackoverflow.com/questions/46157257/pygame-choose-color-nameerror
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Snake")


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    screen.fill(white)
    pygame.display.update()


pygame.quit()