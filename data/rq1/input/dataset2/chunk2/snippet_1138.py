#Source: https://stackoverflow.com/questions/21609227/python-3-3-3-typeerror-list-indices-must-be-integers-not-float
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/images/moon.jpg')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self, surface):
        surface.blit(self.image, self.rect)