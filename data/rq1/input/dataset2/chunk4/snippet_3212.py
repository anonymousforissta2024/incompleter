#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
import pygame
import car
import debris

pygame.init()

#screen settings
WIDTH = 1000
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AutoPilot")
screen.fill((255, 255, 255))

#fps
FPS = 120
clock = pygame.time.Clock()

#load images
bg = pygame.image.load('background/street.png').convert_alpha() # background

#define game variables


######################CAR/DEBRIS##########################

player = car.Player(1, 5)
debris = debris.Debris(1, 5)

##########################################################

#groups
bullet_group = pygame.sprite.Group()
debris_group = pygame.sprite.Group()

debris_group.add(debris)

#game runs here
run = True
while run:

    #draw street
    screen.blit(bg, [0, 0])

    #update groups
    bullet_group.update()
    bullet_group.draw(screen)

    #draw debris
    debris.draw()

    #draw car
    player.draw()
    player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #check if key is down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_a:
                player.movingLeft = True
            if event.key == pygame.K_d:
                player.movingRight = True
            if event.key == pygame.K_SPACE:
                player.shoot()

        #check if key is up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.movingLeft = False
            if event.key == pygame.K_d:
                player.movingRight = False

    #update the display
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()