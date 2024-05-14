#Source: https://stackoverflow.com/questions/68157511/typeerror-when-drawing-circle-in-pygame
import pygame

def Circle(screen,body,fixture,PPM):
    shape = fixture.shape
    radius = shape.radius
    position = (int(body.position.x * PPM),int(body.position.y * PPM))
    
    pygame.draw.circle(screen, (255,0,0), position, radius)


def Draw(screen,PPM,bodies):
    for body in bodies:
        for fixture in body.fixtures:
            try:
                Circle(screen,body,fixture,PPM)
            except: pass
            Circle(screen,body,fixture)