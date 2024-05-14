#Source: https://stackoverflow.com/questions/67491264/typeerror-exceptions-must-derive-from-baseexception-im-trying-to-pause-my-ga
import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2
from pathlib import *

cell_size = 40
cell_number = 19
screen_color = (175, 215, 70)
snake_color = (183, 111, 122)
food_color = (70, 70, 214)
score_color = (56, 76, 11)
score_bg_color = (167, 211, 65)

pygame.init()
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
base_directory = Path(__file__).parent.absolute()
apple_path = 'snake2_resources/images/apple.png'
apple = pygame.image.load(base_directory / apple_path).convert_alpha()
font_path = base_directory / 'snake2_resources/font/poetsen_one_regular.ttf'
game_font = pygame.font.Font(font_path, 24)
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.snake_body = [Vector2(5, 10),Vector2(4, 10),Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_body = False
        snake_path = base_directory / 'snake2_resources/images/snake'

        self.head_up = pygame.image.load(snake_path / 'head_up.png').convert_alpha()
        self.head_down = pygame.image.load(snake_path / 'head_down.png').convert_alpha()
        self.head_right = pygame.image.load(snake_path / 'head_right.png').convert_alpha()
        self.head_left = pygame.image.load(snake_path / 'head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load(snake_path / 'tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(snake_path / 'tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(snake_path / 'tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(snake_path / 'tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load(snake_path / 'body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(snake_path / 'body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load(snake_path / 'body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(snake_path / 'body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(snake_path / 'body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(snake_path / 'body_bl.png').convert_alpha()

    def update_snake_head(self):
        head_direction = self.snake_body[1] - self.snake_body[0]

        if head_direction == Vector2(1, 0):
            self.head = self.head_left
        elif head_direction == Vector2(-1, 0):
            self.head = self.head_right
        elif head_direction == Vector2(0, 1):
            self.head = self.head_up
        elif head_direction == Vector2(0, -1):
            self.head = self.head_down

    def update_snake_tail(self):
        tail_direction = self.snake_body[-2] - self.snake_body[-1]

        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_direction == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_direction == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_direction == Vector2(0, -1):
            self.tail = self.tail_down
    
    def draw_snake(self):
        self.update_snake_head()
        self.update_snake_tail()

        for index, body_part in enumerate(self.snake_body):
            body_part_x = body_part.x * cell_size
            body_part_y = body_part.y * cell_size
            body_part_surface = pygame.Rect(body_part_x, body_part_y, cell_size, cell_size)
            
            if index == 0:
                screen.blit(self.head, body_part_surface)

            elif index == len(self.snake_body) - 1:
                screen.blit(self.tail, body_part_surface)

            else:
                previous_body_part = self.snake_body[index + 1] - body_part
                next_body_part = self.snake_body[index - 1] - body_part

                if previous_body_part.x == next_body_part.x:
                    screen.blit(self.body_vertical, body_part_surface)

                elif previous_body_part.y == next_body_part.y:
                    screen.blit(self.body_horizontal, body_part_surface)

                else:
                    if previous_body_part.x == -1 and next_body_part.y == -1 or previous_body_part.y == -1 and next_body_part.x == -1:
                        screen.blit(self.body_tl, body_part_surface)

                    elif previous_body_part.x == -1 and next_body_part.y == 1 or previous_body_part.y == 1 and next_body_part.x == -1:
                        screen.blit(self.body_bl, body_part_surface)

                    elif previous_body_part.x == 1 and next_body_part.y == -1 or previous_body_part.y == -1 and next_body_part.x == 1:
                        screen.blit(self.body_tr, body_part_surface)
                    
                    elif previous_body_part.x == 1 and next_body_part.y == 1 or previous_body_part.y == 1 and next_body_part.x == 1:
                        screen.blit(self.body_br, body_part_surface)

    def add_body(self):
        self.new_body = True
    
    def move_snake(self):
        if self.new_body == True:
            snake_body_copy = self.snake_body[:]
            snake_body_copy.insert(0, snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]
            self.new_body = False
    
        else:
            snake_body_copy = self.snake_body[: -1]
            snake_body_copy.insert(0, snake_body_copy[0] + self.direction)
            self.snake_body = snake_body_copy[:]

    def reset(self):
        self.snake_body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

class Food:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        food_surface = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(apple, food_surface)

    def randomize(self):
        self.food_x = random.randint(0, cell_number - 1)
        self.food_y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.food_x, self.food_y)

class Game_Snake2:
    def __init__(self):
        self.screen_update = pygame.USEREVENT
        pygame.time.set_timer(self.screen_update, 156)
        self.snake = Snake()
        self.food = Food()
        self.pause = False

    def draw_grass(self):
        grass_color = (167, 209, 61)
        
        for row in range(cell_number):
            if row % 2 == 0:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grass_surface = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_surface)

            else:
                for column in range(cell_number):
                    if column % 2 != 0:
                        grass_surface = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_surface)
    
    def display_score(self):
        score = str(len(self.snake.snake_body) - 3)
        score_surface = game_font.render(score, True, score_color)
        score_x = cell_size * cell_number - 60
        score_y = cell_size * cell_number - 40
        score_shape = score_surface.get_rect(center=(score_x, score_y))
        score_apple = apple.get_rect(midright = (score_shape.left, score_shape.centery))
        score_background = pygame.Rect(score_apple.left, score_apple.top, score_apple.width + score_shape.width + 6, score_apple.height)
        
        pygame.draw.rect(screen, score_bg_color, score_background)
        screen.blit(score_surface, score_shape)
        screen.blit(apple, score_apple)
        pygame.draw.rect(screen, score_color, score_background, 2)
    
    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.food.draw_food()
        self.display_score()
    
    def play_sound(self, sound_name):
        sound_path = base_directory / f'snake2_resources/sounds/{sound_name}.mp3'
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    
    def is_hit(self):
        if self.food.position == self.snake.snake_body[0]:
            self.food.randomize()
            self.snake.add_body()
            self.play_sound('ding')

        for body_part in self.snake.snake_body[1:]:
            if body_part == self.food.position:
                self.food.randomize()

    def game_over(self):
        if not 0 <= self.snake.snake_body[0].x < cell_number or not 0 <= self.snake.snake_body[0].y < cell_number:
            self.play_sound('crash')
            raise 'Game Over!'
            # self.snake.reset()

        for tail in self.snake.snake_body[1:]:
            if tail == self.snake.snake_body[0]:
                raise 'Game Over!'
                # self.snake.reset()

    def update_screen(self):
        self.snake.move_snake()
        self.is_hit()
        self.game_over()
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    
                    if event.key == K_RETURN:
                        # pygame.mixer.music.unpause()
                        self.pause = False
                        self.snake.reset()
                    
                    if not self.pause:
                        if event.key == pygame.K_UP:
                            if game.snake.direction.y != 1:
                                game.snake.direction = Vector2(0, -1)

                        if event.key == pygame.K_DOWN:
                            if game.snake.direction.y != -1:
                                game.snake.direction = Vector2(0, 1)

                        if event.key == pygame.K_LEFT:
                            if game.snake.direction.x != 1:
                                game.snake.direction = Vector2(-1, 0)

                        if event.key == pygame.K_RIGHT:
                            if game.snake.direction.x != -1:
                                game.snake.direction = Vector2(1, 0)
            
                elif event.type == self.screen_update:
                    self.update_screen()
                
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                try:
                    if not self.pause and event.type == self.screen_update:
                        self.update_screen()

                except Exception:
                    self.display_score()
                    self.pause = True

            screen.fill(screen_color)
            self.draw_elements()
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
    game = Game_Snake2()
    game.run()