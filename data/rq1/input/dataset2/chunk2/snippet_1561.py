#Source: https://stackoverflow.com/questions/45908420/python-pygame-attributeerror-int-object-has-no-attribute-draw
import pygame
import random

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

class Rectangle():
    def __init__(self):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 500)
        self.height = random.randrange(20, 70)
        self.width = random.randrange(20, 70)
        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        pygame.draw.rect(screen, GREEN, [self.x, self.y, self.width, self.height])

my_list = []

for number in range(10):
    my_object = Rectangle()
    my_list.append(my_object)

pygame.init()

screen = pygame.display.set_mode((700, 500))  
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for i in range(len(my_list)):
        number.draw()
        number.move()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()