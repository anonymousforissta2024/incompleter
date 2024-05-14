#Source: https://stackoverflow.com/questions/41974709/typeerror-module-object-is-not-callable
import pygame
import pytmx

pygame.init()

class tiledMap():
    def __init__(self):
        self.gameMap = pytmx.load_pygame("maps\_testingMap.tmx")
        self.mapWidth = self.gameMap.width * self.gameMap.tilewidth
        self.mapHeight = self.gameMap.height * self.gameMap.tilewidth

    def render(self, surface):
        for layer in self.gameMap.visible_layers:
            for x,y,gid in layer:
                tile = pytmx.get_tile_image_by_gid(gid)
                surface.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))

    def makeSurface(self):
        tiledSurface = pygame.surface((self.mapWidth, self.mapWidth))
        self.render(tiledSurface)
        return tiledSurface