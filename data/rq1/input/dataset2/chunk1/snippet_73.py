#Source: https://stackoverflow.com/questions/32294479/typeerror-draw-missing-1-required-positional-argument-surface
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.width = width

screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# Sprites lists
all_sprites_list = pygame.sprite.Group

# Create the player
block_width = 30
block_height = 15
player = Block(BLUE, block_width, block_height)
# Set the initial position for the player in the center of the screen
player.rect.x = screen_width/2 - block_width/2
player.rect.y = screen_height/2 - block_height/2
# Add the player to all_sprites_list
all_sprites_list.add(player)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    all_sprites_list.draw(screen)

    pygame.display.flip()