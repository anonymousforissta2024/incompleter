#Source: https://stackoverflow.com/questions/64728441/python-crash-course-alien-invasion-attributeerror-bullet-object-has-no-attr
import pygame
from bullet import Bullet

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet =  Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship, ai_settings, screen, bullets)
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
           if event.key == pygame.K_RIGHT:
             ship.moving_right = False

           elif event.key == pygame.K_LEFT:
             ship.moving_left = False

def update_screen(ai_settings, bullets, screen, ship):

    for bullet in bullets.sprites():
        bullet.draw_bullet()
        ship.blitme()