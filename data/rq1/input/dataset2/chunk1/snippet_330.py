#Source: https://stackoverflow.com/questions/44471789/python-typeerror-argument-1-must-be-pygame-surface-not-pygame-rect
import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
circle = pygame.draw.circle(screen, [255,0,0],[100,100],30,0)
x = 50
y = 50
x_speed = 5
y_speed = 5

done = "False"
while done == "False":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done="True"
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,30,30],0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 30 or x < 0:
        x_speed = -x_speed
    if y > screen.get_height() - 30 or y < 0:
        y_speed = -y_speed
    screen.blit(circle,[x,y])
    pygame.display.flip()

pygame.quit()