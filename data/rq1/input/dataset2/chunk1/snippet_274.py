#Source: https://stackoverflow.com/questions/62823806/random-brick-color-typeerror-pygame-color-object-is-not-callable
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:33:50 2020

@author: 
"""


# example from the Sloan Kelly book
# very slightly modified

# imports (or makes usable) external packages that may be 3rd party (such as pygame)
import pygame, sys, random

# enable "short-hand" notation for imported stuff
from pygame.locals import QUIT, MOUSEBUTTONUP, MOUSEMOTION, KEYDOWN, K_ESCAPE
from pygame import display



#Functions

def draw_bricks():
        for b in bricks:
            windowSurfaceObj.blit(brick[0], b) # makes a copy of brick image acording to coordinates, where stuff is drawn!
        
def draw_bat():
          windowSurfaceObj.blit(bat, batRect)
      
def draw_ball():
          windowSurfaceObj.blit(ball, ballRect)


def brick_color():
    color_var = random.randint(0,3)
    
    if color_var == 0: #red
        brick_color = pygame.Color(198,44,58)
    elif color_var == 1:#blue
        brick_color = pygame.Color(1,128,181)
    elif color_var == 2:#yellow
        brick_color = pygame.Color(255,211,92)
    elif color_var == 3:#green
        brick_color = pygame.Color(0,157,103)
    return brick_color









pygame.init()
fpsClock = pygame.time.Clock()


# new and improved:
# create surface object aka. the main window
inf = display.Info()
screen_width = inf.current_w - 200 # make window sizea little bit smaller than actual screen
screen_height = inf.current_h - 200
# windowSurfaceObj = display.set_mode(size=(screen_width, screen_height), flags=pygame.FULLSCREEN) # initialize window
windowSurfaceObj = display.set_mode(size=(screen_width, screen_height)) # initialize window

display.set_caption('New and improved Bricks'); # set window title

# brick layout

brick_width = 50
brick_height = 20
num_bricks_in_row = 7
num_brick_rows = 5
brick_row_height = 2 * brick_height
brick_offset_y = 100
brick_column_width = 2 * brick_width
brick_offset_x = int(screen_width/2 - brick_column_width*num_bricks_in_row/2) # place it in the middle of the screen
brick_color = brick_color()

# ball related stuff

ball_radius = int(screen_height/200)

# more game constants!

fps = 60 # desired frames per second
background_colour = pygame.Color(0, 0, 0) # background is black

# used variables for bat dimensions
bat_width = 100
bat_height = 10

# ball related stuff
ball_start_x = 24 # somehwere near the left of the window
ball_start_y = 200 # initial ball position when new ball is released
ball_speed = int(fps*0.15) # speed of ball in pixel per frame! use fps var. here to make real ball speed independent of frame rate


# bat init

# replace bat with crude hand drawn one

batcolor = pygame.Color(0, 0, 255) # bat color: blue!
bat = pygame.Surface([bat_width, bat_height]) # this Surface is for drawing the bat upon
pygame.draw.rect(bat, batcolor, [0, 0, bat_width, bat_height]) # draw bat. It's a simple rectangle.
bat = bat.convert_alpha() # deal with transparency

# place the bat somewhere near the bottom of the screen/window
player_start_x = 0 # initial position is on left
player_start_y = screen_height - 6 * bat_height # this is used as Y coordinate for bat, near the bottom of the screen

batRect = bat.get_rect() # rectangle around bat, used to move it around later
mousex = player_start_x
mousey = player_start_y # mousex and mousey later used for moving the bat around, not actual mouse coordinates at this point

# ball init

ball_color = pygame.Color(255, 255, 255) # white
ball = pygame.Surface([ball_radius*2, ball_radius*2]) # Surface for drawing the ball upon
pygame.draw.circle(ball, ball_color, (ball_radius, ball_radius), ball_radius) # draw circle on ball surface

ballRect = ball.get_rect() # rectangle around ball, use to move it around later
ballServed = False
bx = ball_start_x # bx is actual ball postion
by = ball_start_y # by is actual (current) ball position
sx = ball_speed # current ball speed in horizontal direction
sy = ball_speed # current ball speed vertical
ballRect.topleft = (bx, by) # move ball rectangle to initial position

# brick init
brick = pygame.Surface([brick_width, brick_height]),brick_color # surface for a single brick
pygame.draw.rect(brick[0], brick[1], [0, 0, brick_width, brick_height])



bricks = [] # list of *coordinates* of the bricks

# initialize coordinates of bricks

for y in range(num_brick_rows):
    brickY = (y * brick_row_height) + brick_offset_y    
    for x in range(num_bricks_in_row):
        brickX = (x * brick_column_width) + brick_offset_x
        color_of_brick = brick_color()
        bricks.append((brickX, brickY),color_of_brick) # coordinates are in fact tuples (x,y)

while True: # main loop, run once per frame (i.e. fps times per second)
    
    windowSurfaceObj.fill(background_colour) # clear the screen

    # brick draw
    # for b in bricks: # remember: bricks is a list of brick coordinates, not surfaces
    #     windowSurfaceObj.blit(brick, b) # make copy of brick image and place it on screen, b = brick coordinates
    draw_bricks()
    
    # bat and ball draw, rectangles around bat and ball are used for positioning
    # windowSurfaceObj.blit(bat, batRect) # copy surface with image of bat to screen
    # windowSurfaceObj.blit(ball, ballRect) # same for ball
    draw_bat()
    draw_ball()
    
    # main event loop
    # process user interaction
    for event in pygame.event.get():
        # quit the game if window is closed or escape key is pressed
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP and not ballServed:
            ballServed = True # start game, when mouse is clicked
        elif event.type == MOUSEMOTION: # mouse has moved
            mousex, mousey = event.pos # set mouse coordinate variables to actual mouse coordinates
            if mousex < screen_width - bat_width:
                  if mousex < 0: # may occur in full screen / large window mode
                      batRect.topleft = (0, player_start_y)
                  else:
                      batRect.topleft = (mousex, player_start_y)
            else:
                batRect.topleft = (screen_width - bat_width, player_start_y)
    
    # main game logic 
    if ballServed: # if game is in progress
        ballRect.topleft = (bx, by) # position the ball using its rectangle
        bx += sx # sx = speed of the ball in X direction
        by += sy # sy = speed of the ball in Y direction
    
    if (by >= screen_height): # ball below bottom of screen
        ballServed = False # game not in progess, ball lost!
        bx, by = (ball_start_x, ball_start_y) # ball is reset to start position
        ballRect.topleft = (bx, by) # move the rectangle around ball to correct position
        
    if by <= 0: # ball hits top
        by = 0
        sy *= -1 # reflect
        
    if bx <= 0: # ball hits left side of window
        bx = 0
        sx *= -1 # reflect
        
    if bx >= screen_width - ball_radius*2: # ball hits right side of window
        bx = screen_width - ball_radius*2
        sx *= -1 # reflection
    
    # collision detection
    brickForRemoval = None
        
    for b in bricks: # remember: bricks is list of coordinates of bricks; iterating all bricks and check each one for collision
        briX, briY = b # tuple unwrapping: x and y coordinates of top left of brick
        if bx + ball_radius*2 >= briX and bx <= briX + brick_width: # is x coordinate of ball inside brick (or touching brick)
            if (by + ball_radius*2 >= briY and by <= briY + brick_height): # same for y coordinate
                brickForRemoval = b # brick was hit and is scheduled for removal
                if bx <= briX + ball_radius*2: # ball hit brick from left
                    sx *= -1 # reflect
                elif bx >= briX + brick_width - ball_radius*2: # ball hit brick from right
                    sx *= -1 # reflect
                    
                if by <= briY + ball_radius * 2: # ball hit brick from top
                    sy *= -1 # reflect
                elif by >= briY + brick_height - ball_radius*2: # ball hit brick from below
                    sy *= -1 # reflect
                break # ball hit a brick and cannot hit another one at the same time
        
    if brickForRemoval != None: # if a brick is scheduled for removal…
        bricks.remove(brickForRemoval) # … remove it!
        
        
    # collision check: does bat hit ball?
    if (bx >= mousex and bx <= mousex + bat_width): # using bat_width variable
        if(by >= player_start_y - bat_height and by <= player_start_y):
            sy *= -1 # reflect
            
    pygame.display.update() # show updated screen
    fpsClock.tick(fps) # limit fps