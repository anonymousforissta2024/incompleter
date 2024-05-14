#Source: https://stackoverflow.com/questions/70369987/typeerror-changespeed-takes-2-positional-arguments-but-3-were-given
import pygame
import random

#-------------------------BUGS I NEED TO FIX-------------------------#
#CANNOT MOVE CHARACTER


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255,255,0)
score = 0
play = 0
progress = 0
errorkey = 0
helpme = 0
score1 = 0

#stop = 0

def levelsetup():
    testman.rect.x = 0
    one.rect.x = 460
    two.rect.x = 530
    three.rect.x = 615
    four.rect.x = 700
    for crate in crate_list:
            crate.rect.x -= rect_x_change
    screen.blit(user_interface, [0,0])
    lvlselect.draw(screen)
    font = pygame.font.SysFont('comicsansms', 65, True, False)
    playscore = font.render(str(score1), True, BLACK)
    playhealth = font.render(str(testman.health), True, BLACK)
    screen.blit(playhealth, [30,392])
    screen.blit(playscore, [205,392])
    playersprite.draw(screen)
    crate_list.draw(screen)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.health = 100
        self.rect.x = 0
        self.change_x = 0
class Player(Sprite):
    def update(self):
 
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Now see how the mouse position is different from the current
        # player position. (How far did we move?)
        diff_x = self.rect.x - pos[0]
        diff_y = self.rect.y - pos[1]
 
        # Loop through each block that we are carrying and adjust
        # it by the amount we moved.
        self.rect.x += self.change_x
        
        # Now wet the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def changespeed(self, x):
        self.change_x += x
        
 
class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

pygame.mixer.pre_init(44100, -16, 1, 512)
# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 750
screen_height = 500

screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("LARP")

item_crate = pygame.image.load("crate.png").convert_alpha()
crate_list = pygame.sprite.Group()


def blit_text(surface, text, pos, font, color=pygame.Color('WHITE')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = 83
        #y = 80# Reset the x.
        y += word_height  # Start on new row.

text = "\n\n\nUnless you're a teacher I have no clue how you got this game.\nBut that doesn't matter. After your character received a\nmysterious LARP invitation in the forest he finds that the\ndevious Wendyl has turned the LARP group into an\nauthoritarian regime! It's your job to stop Wendyl and anyone\nin your way!"
text2 = "\n\n\n\n\n\n\n\n\nLEFT ARROW KEY - MOVE LEFT\nRIGHT ARROW KEY - MOVE RIGHT\nCLICK MOUSE - FIRE WEAPON/SELECT OPTION\nMOVE MOUSE - CURSOR/AIMING"

font = pygame.font.SysFont('comicsansms', 20)
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
#TITLE SCREEN
title_image = pygame.image.load("title.png").convert_alpha()
quit_image = pygame.image.load("quit.png").convert_alpha()
logo_image = pygame.image.load("logo.png").convert_alpha()
background_image = pygame.image.load("title_screen.png").convert_alpha()
map_image = pygame.image.load("map.png").convert_alpha()
quit_block = pygame.sprite.Group()
start_block = pygame.sprite.Group()
Title = pygame.mixer.Sound("title_song.ogg")
Map = pygame.mixer.Sound("map_song.ogg")
help_image = pygame.image.load("help.png").convert_alpha()
help_title = pygame.sprite.Group()



#PLAYER
player_image = pygame.image.load("player.png").convert_alpha()
#testman = pygame.image.load("testman.png").convert_alpha()
testman = Sprite("testman.png")
playersprite = pygame.sprite.Group()
playersprite.add(testman)
testman.rect.y = 230


#CUTSCENES
cutscene_2 = pygame.image.load("cutscene_2.png").convert_alpha()
cutscene_1 = pygame.image.load("cutscene_1.png").convert_alpha()
continue_button = pygame.image.load("cont.png").convert_alpha()
continue_list = pygame.sprite.Group()

#NUMBERS
one = Sprite("one.png")
two = Sprite("two.png")
three = Sprite("three.png")
four = Sprite("four.png")
butt_one = pygame.sprite.Group()
butt_two = pygame.sprite.Group()
butt_three = pygame.sprite.Group()
butt_four = pygame.sprite.Group()
lvlselect = pygame.sprite.Group()

#OTHER
back_button = pygame.image.load("back.png").convert_alpha()
back_butt = pygame.sprite.Group()
stage_error = pygame.image.load("stage_progess_error.png").convert_alpha()
stage_error = pygame.sprite.Group()
programIcon = pygame.image.load('imggg.png')

map_screen = pygame.sprite.Group()

#STAGES
stage_one = pygame.image.load("level_1.png").convert_alpha()
stage_one_music = pygame.mixer.Sound("stage_1.ogg")

#USER INTERFACE
user_interface = pygame.image.load("ui.png").convert_alpha()

# This is a list of every sprite.
# All blocks and the player block as well.
player_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 

#TITLE SCREEN
title = Sprite("title.png")
title.rect.x = 340
title.rect.y = 220
all_sprites_list.add(title)
start_block.add(title)
quitg = Sprite("quit.png")
quitg.rect.x = 340
quitg.rect.y = 360
all_sprites_list.add(quitg)
quit_block.add(quitg)
logo = Sprite("logo.png")
logo.rect.y = 100
logo.rect.x = 317
all_sprites_list.add(logo)
block_list.add(logo)
help_image = Sprite("help.png")
help_image.rect.x = 340
help_image.rect.y = 290
all_sprites_list.add(help_image)
help_title.add(help_image)

#CUTSCENE
continues = Sprite("cont.png")
continues.rect.x = 608
continues.rect.y = 466
continue_list.add(continues)

#NUMBERS
one = Sprite("one.png")
butt_one.add(one)
butt_two.add(two)
butt_three.add(three)
butt_four.add(four)
lvlselect.add(one)
lvlselect.add(two)
lvlselect.add(three)
lvlselect.add(four)

#OTHER
back = Sprite("back.png")
back.rect.x = 0
back.rect.y = 12
back_butt.add(back)
error = Sprite("stage_progess_error.png")
error.rect.x = 100
error.rect.y = 85
stage_error.add(error)

map_image = Sprite("map.png")
map_screen.add(map_image)
pygame.display.set_icon(programIcon)

#PLAYER
player = Player("player.png")
player_list.add(player)
all_sprites_list.add(player)



rect_x = 0
rect_x_change = 1.65
for i in range(5):
    crate = Sprite("crate.png")
    cratex = random.randint(2000,18000)
    crate.rect.x = cratex
    crate.rect.y = 245
    crate_list.add(crate)
    print(crate.rect.x, crate.rect.y)
    
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(False)

 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play == 0:
                help_block_hit = pygame.sprite.spritecollide(player, help_title, False)
                if len(help_block_hit) >= 1:
                    helpme += 1
                
                start_block_hit = pygame.sprite.spritecollide(player, start_block, False)
                if len(start_block_hit) >= 1:
                    play += 1

                quit_block_hit = pygame.sprite.spritecollide(player, quit_block, False)
                if len(quit_block_hit) >= 1:
                    done = True
                if helpme == 1:
                    back_butt_hit = pygame.sprite.spritecollide(player, back_butt, False)
                    if len(back_butt_hit) >= 1:
                        helpme = 0
            elif play == 1:
                continue_block_hit = pygame.sprite.spritecollide(player, continue_list, False)
                if len(continue_block_hit) >= 1:
                    play += 1
                    
            elif play == 2:
                if len(continue_block_hit) >= 1:
                    play += 1
                    
            elif play == 3:
                back_butt_hit = pygame.sprite.spritecollide(player, back_butt, False)
                if len(back_butt_hit) >= 1:
                    play = 0

                map_hit = pygame.sprite.spritecollide(player, map_screen, False)
                if len(map_hit) >= 1:
                    errorkey = 0

                one_butt_hit = pygame.sprite.spritecollide(player, butt_one, False)
                if len(one_butt_hit) >= 1:
                    play = 4
                    
                two_butt_hit = pygame.sprite.spritecollide(player, butt_two, False)
                if len(two_butt_hit) >= 1:
                    if progress == 0:
                        errorkey = 1
                three_butt_hit = pygame.sprite.spritecollide(player, butt_three, False)
                if len(three_butt_hit) >= 1:
                    if progress == 0 or progress == 1:
                        errorkey = 1
                four_butt_hit = pygame.sprite.spritecollide(player, butt_four, False)
                if len(four_butt_hit) >= 1:
                    if progress == 0 or progress == 1 or progress == 2:
                        errorkey = 1
            elif play == 4:
                crate_hit = pygame.sprite.spritecollide(player, crate_list, True)
                if len(crate_hit) >= 1:
                    score1 += 100
                    testman.health += 5
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                testman.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                testman.change_x(3, 0)
 
        #elif event.type == pygame.MOUSEBUTTONUP:

 
    all_sprites_list.update()

   
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw all the spites
    if play == 0:
        screen.blit(background_image, [0,0])
        if helpme == 0: 
            all_sprites_list.draw(screen)
            Map.stop()
            Title.play()
        elif helpme == 1:
            back.rect.x = 0
            back.rect.y = 0
            pygame.draw.rect(screen, BLACK, [80,60,600,420])
            pygame.draw.rect(screen, WHITE, [80,280,600,10])
            fontheader = pygame.font.SysFont('comicsansms', 25, True, False)
            textheader = fontheader.render("Welcome to LARP!", True, WHITE)
            screen.blit(textheader, [255,60])
            back_butt.draw(screen)
            blit_text(screen, text, (20, 20), font)
            blit_text(screen, text2, (50,50), font)
        
    elif play == 1:
        screen.blit(cutscene_2, [0,0])
        continue_list.draw(screen)
        
    elif play == 2:
        screen.blit(cutscene_1, [0,0])
        continue_list.draw(screen)
        
    elif play == 3:
        back.rect.x = 0
        back.rect.y = 12
        one.rect.x = 55
        one.rect.y = 410
        two.rect.x = 250
        two.rect.y = 410
        three.rect.x = 466
        three.rect.y = 410
        four.rect.x = 660
        four.rect.y = 410
        map_screen.draw(screen)
        back_butt.draw(screen)
        lvlselect.draw(screen)
        Title.stop()
        Map.play()
        if errorkey == 1:
            stage_error.draw(screen)
    #STAGE 1
    elif play == 4:
        Map.stop()
        Title.stop()
        stage_one_music.play()
        rect_x -= rect_x_change
        screen.blit(stage_one, [rect_x,-180])
        levelsetup()
        if testman.health >= 100:
            testman.health = 100
    elif play == 5:
        levelsetup()
        
    screen.blit(player_image, [player.rect.x, player.rect.y])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()