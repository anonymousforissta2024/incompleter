#Source: https://stackoverflow.com/questions/64795214/why-am-i-getting-nameerror-wolf-is-not-defined
import pygame
import random
import Colors
import Player
import Enemy
        
# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width  = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

#SPRITE LIST CREATIONS
wolf_list = pygame.sprite.Group()
poison_wolf_list = pygame.sprite.Group()
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a single block
    wolf = Wolf(Colors.GREEN, 20, 15)
    # Set a random location for the block
    wolf.rect.x = random.randrange(screen_width)
    wolf.rect.y = random.randrange(screen_height)
    # Add the block to the list of objects
    wolf_list.add(wolf)
    all_sprites_list.add(wolf)
    
for i in range(50):
    # This represents a single block
    wolf = Wolf(Colors.RED, 20, 15)
    # Set a random location for the block
    wolf.rect.x = random.randrange(screen_width)
    wolf.rect.y = random.randrange(screen_height)
    # Add the block to the list of objects
    poison_wolf_list.add(wolf)
    all_sprites_list.add(wolf)
    #Since this will repeat 50 times, you will create 50 red blocks
    #This adds all 50 blocks to the bad_block_list, and the all_sprites_list.
 
# Create a RED player block
player = Player.Player(100, 100)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -3)
            elif event.key == pygame.K_s:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 3)
            elif event.key == pygame.K_s:
                player.changespeed(0, -3)

    # Clear the screen
    screen.fill(Colors.WHITE)
 
    # Game Logic
    all_sprites_list.update()

 
    # See if the player block has collided with anything.
    wolf_list = pygame.sprite.spritecollide(player, wolf_list, True)
    poison_wolf_list = pygame.sprite.spritecollide(player, poison_wolf_list, True)
    # Check the list of collisions.
    for block in wolf_list:
        score += 1
        print(score)
    for block in poison_wolf_list:
        score -= 1
        print(score) 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()