#Source: https://stackoverflow.com/questions/67459471/attributeerror-pygame-math-vector2-object-has-no-attribute
import pygame, sys
from pygame.locals import *
from pygame.math import Vector2

class Food:
    def __init__(self):
        self.food_x = 5
        self.food_y = 4
        self.position = Vector2(self.food_x, self.food_y)

    def draw_food(self):
        food_shape = pygame.Rect(self.position.food_x, self.position.food_y, cell_size, cell_size)
        pygame.draw.rect(screen, screen_surface_color, food_shape)

cell_size = 40
cell_number = 19
screen_color = (175, 215, 70)
screen_surface_color = (70, 70, 214)

pygame.init()
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(screen_color)
    food.draw_food()
    pygame.display.update()
    clock.tick(60)