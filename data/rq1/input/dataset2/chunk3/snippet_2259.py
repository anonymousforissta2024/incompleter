#Source: https://stackoverflow.com/questions/64728441/python-crash-course-alien-invasion-attributeerror-bullet-object-has-no-attr
import sys
import game_functions as gf
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
# Initialize pygame, settings, and screen object.
 pygame.init()
 ai_settings = Settings()



screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")

screen.fill(ai_settings.bg_color)
# Make a ship.
ship = Ship(screen, ai_settings)
bullets = Group()

# Background color
bg_color = (230, 230, 230)


while True:

    gf.check_events(ai_settings, screen, ship, bullets)
    gf.update_screen(ai_settings, bullets, screen, ship)

    gf.check_events(ship, screen, ship, bullets)
    ship.update(ai_settings)
    bullets.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(ai_settings.bg_color)

    ship.blitme()
    pygame.display.flip()

run_game()