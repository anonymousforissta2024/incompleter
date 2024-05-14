#Source: https://stackoverflow.com/questions/31484492/typeerror-argument-1-must-be-pygame-surface-not-function
import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Le jeux')
clock = pygame.time.Clock()

thatonething = pygame.image.load('thatonething.png')

def somefunction(x,y):
    gameDisplay.blit(thatonething,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event) #This creates a log of the events that pygame has been handling.

    gameDisplay.fill(white)
    somefunction(x,y)
    pygame.display.update() #Updates everything "pygame.display.flip()" updates just one thing
    clock.tick(30) #This defines the refresh rate i.e. 30 in brackets gives 30 fps

pygame.quit() #Closes the game (with the next line)
quit()