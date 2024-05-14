#Source: https://stackoverflow.com/questions/11825053/pygame-typeerror-int-object-is-not-callable
import pygame
import sys 

pygame.init()
screen = pygame.display.set_mode((600,400))
bg = pygame.image.load('bg.jpg')
player = pygame.image.load('player.jpg')
pos = player.get_rect()

while True:
    for i in pygame.event.get():
       if i.type() == pygame.QUIT:
            sys.exit()
    screen.blit(bg,(0,0))
    screen.blit(player,(i,i))
    pygame.display.update()