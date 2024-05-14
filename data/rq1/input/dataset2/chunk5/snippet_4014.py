#Source: https://stackoverflow.com/questions/41974709/typeerror-module-object-is-not-callable
import pygame
from settings import *
from loading import *

class game():
    def __init__(self):
        self.screen = pygame.display.set_mode((displayWidth, displayHeight))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.gameRunning = True

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False

    def gameLoop(self):
        self.clock.tick(fps)
        self.loop()
        self.loadMap()
        self.editScreen()

    def editScreen(self):
        self.screen.blit(self.map_img, (0,0))
        pygame.display.update()

    def loadMap(self):
        self.map = tiledMap()
        self.map_img = self.map.makeSurface()

playGame = game()
while playGame.gameRunning == True:
    playGame.gameLoop()