#Source: https://stackoverflow.com/questions/33182865/pygame-help-typeerror-add-argument-after-must-be-a-sequence-not-pygame-s
import pygame    

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('Mugger Space Cadet.jpg')
        self.rect = pygame.rect.Rect((16, 32), self.image.get_size())

    def update(self, dt, game):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 150 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 150 * dt
        if key[pygame.K_UP]:
            self.rect.y -= 150 * dt
        if key[pygame.K_DOWN]:
            self.rect.y += 150 * dt

        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last

class Game(object):
    def main(self, screen):

        clock = pygame.time.Clock()

        background = pygame.image.load('mockup level.png')
        sprites = pygame.sprite.Group()
#       sprites.add(background)
        self.player = Player(sprites)
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('block.png')
        for x in range(0, 448, 32):
            for y in range(0, 320, 32):
                if x in (0, 448-32) or y in (0, 320-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect= pygame.rect.Rect((x, y), block.get_size())
        sprites.add(self.walls)

        while True:
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            sprites.update(dt / 1000., self)
            screen.blit(background, (0, 0))
            sprites.draw(screen)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((448, 320))
    Game().main(screen)