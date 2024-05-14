#Source: https://stackoverflow.com/questions/60262615/how-to-fix-a-nameerror-name-color-is-not-defined
size = (1280, 850)
Win = pygame.display.set_mode(size)
class Particle:
    color = (255, 255, 0)
    ID = 0

    def __init__(self, rect):
        Particle.ID += 1
        self.color = (color)
        self.ID = Particle.ID
        self.rect = rect

    def move(self, x, y):
        self.rect.move(x, y)

    def draw(self):
        pygame.draw.rect(Win, self.color, self.rect)

    def collide(self, rect1):
        return self.rect.colliderect(rect1)