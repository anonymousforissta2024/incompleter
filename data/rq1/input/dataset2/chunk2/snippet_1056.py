#Source: https://stackoverflow.com/questions/22938809/attributeerror-oandx-object-has-no-attribute-run
import pygame  #provides Pygame framework.
import sys #provides sys.exit function

from pygame import *

from pygame.locals import * # Import constants used by PyGame

# game classes

class OAndX:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Create the clock to manage the game loop
        self.clock = time.Clock()
        display.set_caption("Noughts and Crosses")
        # Create a windows with a resolution of 640 x 480
        self.displaySize=(640,480)
        self.screen=display.set_mode(self.displaySize)
        # will either be 0 or X
        self.player="0"

# The background class

class Background:
    def __init__(self,displaySize):
        self.image=Surface(displaySize)
    # Draw a title
    # Create the font we'll use
        self.font=font.Font(None,(displaySize[0]/12))
        self.text = self.font.render("Noughts and crosses",True,(Color("White")))
        # Work out where to place the text
        self.textRect = self.text.get_rect()
        self.textRect.centerx=displaySize[0] / 2
        # Add a little margin
        self.textRect.top = displaySize[1] * 0.02
        # Blit the text to the background image
        self.image.blit(self.text, self.textRect)
    def draw(self, display):
        display.blit(self.image, (0, 0))

# A class for an individual grid square
class GridSquare(sprite.Sprite):
    def __init__(self, position, gridSize):
        # Initialise the sprite base class
        super(GridSquare, self).__init__()
        # We want to know which row and column we are in
        self.position = position
        # State can be “X”, “O” or “”
        self.state = ""
        self.permanentState = False
        self.newState = ""
        # Work out the position and size of the square
        width = gridSize[0] / 3
        height = gridSize[1] / 3
        # Get the x and y co ordinate of the top left corner
        x = (position[0] * width) - width
        y = (position[1] * height) - height
        # Create the image, the rect and then position the rect
        self.image = Surface((width,height))
        self.image.fill(Color("white"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # The rect we have is white, which is the parent rect
        # We will draw another rect in the middle so that we have
        # a white border but a blue center
        self.childImage = Surface(((self.rect.w * 0.9), (self.rect.h * 0.9)))
        self.childImage.fill(Color("blue"))
        self.childRect = self.childImage.get_rect()
        self.childRect.center = ((width /2), (height / 2))
        self.image.blit(self.childImage,self.childRect)
        # Create the font we’ll use to display O and X
        self.font = font.Font(None, (self.childRect.w))

class Grid:
    def __init__(self, displaySize):
        self.image=Surface(displaySize)
        # Make a number of grid squares
        gridSize = (displaySize[0] * 0.75,displaySize[1] * 0.75)
        # Work out the co-ordinate of the top left corner of the grid so that it can be centered on the screen
        self.position = ((displaySize[0] /2) - (gridSize[0] / 2),(displaySize[1] / 2) - (gridSize[1] / 2))
        # An empty array to hold our grid squares in
        self.squares = []
        for row in range(1,4):
            # Loop to make 3 rows
            for column in range(1,4):
            # Loop to make 3 columns
                squarePosition = (column,row)
                self.squares.append(GridSquare(squarePosition, gridSize))
                # Get the squares in a sprite group
                self.sprites = sprite.Group()
                for square in self.squares:
                    self.sprites.add(square)

    def draw(self, display):
        self.sprites.update()
        self.sprites.draw(self.image)
        display.blit(self.image, self.position)

    def update(self):
        # Need to update if we need to set a new state
        if (self.state != self.newState):
            # Refill the childImage blue
            self.childImage.fill(Color("blue"))
            text = self.font.render(self.newState, True, (Color("white")))
            textRect = text.get_rect()
            textRect.center = ((self.childRect.w / 2),(self.childRect.h / 2))
            # We need to blit twice because the new child image needs to be blitted to the parent image
            self.childImage.blit(text,textRect)
            self.image.blit(self.childImage, self.childRect)
            # Reset the newState variable
            self.state = self.newState
            self.newState = ""
def setState(self, newState,permanent=False):
    if not self.permanentState:
        self.newState = newState
        if permanent:
            self.permanentState = True

def reset(self):
    # Create an instance of our background and grid class
    self.background =Background(self.displaySize)
    self.grid = Grid(self.displaySize)

def getSquareState(self, column, row):
    # Get the square with the requested position
    for square in self.squares:
        if square.position == (column,row):
            return square.state

def full(self):
    # Finds out if the grid is full
    count = 0
    for square in self.squares:
        if square.permanentState ==True:
            count += 1
            if count == 9:
                return True
            else:
                return False

def getWinner(self):
    players = ["X", "O"]
    for player in players:
        # check horizontal spaces
        for column in range (1, 4):
            for row in range (1, 4):
                square1 = self.grid.getSquareState(column, row)
                square2 = self.grid.getSquareState((column + 1),row)
                square3 = self.grid.getSquareState((column + 2), row)
                # Get the player of the square (either O or X)
                if (square1 == player) and (square2 == player) and (square3 == player):
                    return player
                    # check vertical spaces
                    for column in range (1, 4):
                        for row in range (1, 4):
                            square1 = self.grid.getSquareState(column, row)
                            square2 = self.grid.getSquareState(column, (row + 1))
                            square3 = self.grid.getSquareState(column, (row + 2))
                            # Get the player of the square (either O or X)
                            if (square1 == player) and (square2 == player) and (square3 == player):
                                return player
                                # check forwards diagonal spaces
                                for column in range (1, 4):
                                    for row in range (1, 4):
                                        square1 = self.grid.getSquareState(column, row)
                                        square2 = self.grid.getSquareState((column + 1), (row - 1))
                                        square3 = self.grid.getSquareState((column + 2), (row - 2))
                                        # Get the player of the square (either O or X)
                                        if (square1 == player) and (square2 == player) and (square3 == player):
                                            return player
                                            # check backwards diagonal spaces
                                            for column in range (1, 4):
                                                for row in range (1, 4):
                                                    square1 = self.grid.getSquareState(column, row)
                                                    square2 = self.grid.getSquareState((column + 1), (row + 1))
                                                    square3 = self.grid.getSquareState((column + 2), (row + 2))
                                                    # Get the player of the square (either O or X)
                                                    if (square1 == player) and (square2 == player) and (square3 == player):
                                                        return player

                                                        # Check if grid is full if someone hasn’t won already
                                                        if self.grid.full():
                                                            return "draw"

def winMessage(self, winner):
    # Display message then reset the game to its initial state
    # Blank out the screen
    self.screen.fill(Color("Black"))
    # Create the font we’ll use
    textFont = font.Font(None, (self.displaySize[0] / 6))
    textString = ""
    if winner == "draw":
        textString = "It was a draw!"
    else:
        textString = winner + " Wins!"
    # Create the text surface
    text = textFont.render(textString,True,(Color("white")))
    textRect = text.get_rect()
    textRect.centerx = self.displaySize[0] / 2
    textRect.centery = self.displaySize[1] / 2
    # Blit changes and update the display before we sleep
    self.screen.blit(text, textRect)
    display.update()
    # time.wait comes from pygame libs
    time.wait(2000)
    # Set game to its initial state
    self.reset()

def run(self):
    while True:
        # Our Game loop,Handle events
        self.handleEvents()
        # Draw our background and grid
        self.background.draw(self. screen)
        self.grid.draw(self.screen)
        # Update our display
        display.update()
        # Limit the game to 10 fps
        self.clock.tick(10)

def handleEvents(self):
    # We need to know if the mouse has been clicked later on
    mouseClicked = False
    # Handle events, starting with quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            if event.type == MOUSEBUTTONUP:
                mouseClicked = True
                # Get the co ordinate of the mouse mousex, mousey = mouse.get_pos() ,These are relative to the top left of the screen,and we need to make them relative to the top left of the grid
                mousex -= self.grid.position[0]
                mousey -= self.grid.position[1]
                # Find which rect the mouse is in
                for square in self.grid.squares:
                    if square.rect.collidepoint((mousex, mousey)):
                        if mouseClicked:
                            square.setState(self.player, True)
                            # Change to next player
                            if self.player == "O":
                                self.player = "X"
                            else:
                                self.player = "O"
                            # Check for a winner
                            winner = self.getWinner()

                            if winner:
                                self.winMessage(winner)
                            else:
                                square.setState(self.player)
                        else:
                                # Set it to blank, only if
                            permanentState == False
                        square.setState("")

if __name__ == "__main__":
    game = OAndX()
    game.run()