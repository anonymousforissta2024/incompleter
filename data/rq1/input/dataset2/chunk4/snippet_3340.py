#Source: https://stackoverflow.com/questions/77336211/typeerror-invalid-rect-assignment-with-vectors
import pygame
import os
import random

vec = pygame.math.Vector2

WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PongX")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = ()

FPS = 60
VEL = 5
ball_vel = 1

PONG_WIDTH, PONG_HEIGHT = 30, 10
LEFT_PONG_IMAGE = pygame.image.load(os.path.join("Pong", "Pong.png"))
RIGHT_PONG_IMAGE = pygame.image.load(os.path.join("Pong", "Pong.png"))
BALL_WIDTH, BALL_HEIGHT = 10, 10
PONG_BALL_IMAGE = pygame.image.load(os.path.join("Pong", "Pong_Ball.png"))


UP_BORDER = pygame.Rect(0, 640, -2, 2)
DOWN_BORDER = pygame.Rect(0, 640, 478, 482)

def draw_window(left, right, ball):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, UP_BORDER)
    pygame.draw.rect(WIN, WHITE, DOWN_BORDER)
    WIN.blit(PONG_BALL_IMAGE, (ball.x, ball.y))
    WIN.blit(LEFT_PONG_IMAGE, (left.x, left.y))
    WIN.blit(RIGHT_PONG_IMAGE, (right.x, right.y))
    pygame.display.update()

def ball_handle_movement(ball):
    if ball.y == 0 or 480:
        ball.y = vec(random.randint(0, 480), random.randint(0, 480))
    if ball.x == 0 or 640:
        ball.x = vec(random.randint(0, 640), random.randint(0, 640))


def left_handle_movement(keys_pressed, left):
    if keys_pressed[pygame.K_w] and left.y - VEL > 0:
            left.y -= VEL
    if keys_pressed[pygame.K_s] and left.y + VEL + left.height < HEIGHT - 15:
            left.y += VEL

def right_handle_movement(keys_pressed, right):
    if keys_pressed[pygame.K_UP] and right.y - VEL > 0:
            right.y -= VEL
    if keys_pressed[pygame.K_DOWN] and right.y + VEL + right.height < HEIGHT - 15:
            right.y += VEL

def main():
    left = pygame.Rect(30, 210, PONG_WIDTH, PONG_HEIGHT)
    right = pygame.Rect(600, 210, PONG_WIDTH, PONG_HEIGHT)
    ball = pygame.Rect(WIDTH/2, HEIGHT/2 ,BALL_WIDTH, BALL_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



        keys_pressed = pygame.key.get_pressed()
        ball_handle_movement(ball)
        left_handle_movement(keys_pressed, left)
        right_handle_movement(keys_pressed, right)
        draw_window(left, right, ball)

    pygame.quit()

if __name__ == "__main__":
    main()