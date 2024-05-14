#Source: https://stackoverflow.com/questions/54858231/python3-6-and-pyautogui-pixel-commands-typeerror-new-takes-4-position
#
# IMPORT ALL NECESSARY THINGS
#

import os, time, sys, pyautogui as gui, argparse as arg

#
# FAILSAFES
#

gui.FAILSAFE = True
gui.PAUSE = 0.1

#
# SET UP ARGUMENT PARSER
#

parser = arg.ArgumentParser(description='A machine learning script powered by TensorFlow designed to be run on "chess.com" using Python.')
parser.add_argument("-s", "--sleep", nargs='?', type=int, default='5', help='Number of seconds that the program should sleep before starting. This gives you time to move over to the website before the program looks for the gamboard on screen.')
args = parser.parse_args()

#
# ASKS USER FOR WHAT SIDE IT IS ON
#

side = input("Are you white or black?  ")

if side == "W" or side == "w" or side == "white" or side == "White":
     side = "W"
elif side == "B" or side == "b" or side == "black" or side == "Black":
    side = "B"
else:
    print("Invalid selection for which side!")
    side = None
    sys.exit(0)

#
# PRINT "READY" AND THEN WAIT FOR SPECIFIED AMOUNT OF TIME - DEFAULT 5 SECONDS
#

print("Ready! Waiting for " + str(args.sleep) + " seconds!")
time.sleep(int(args.sleep))

#
# GET AREA OF GAMEBOARD ON SCREEN
#

if side == "W":
    gameboard = gui.locateOnScreen('./img/white/chessboard_white.png', confidence=0.55, grayscale=True)
    left = gameboard.left - 10
    top = gameboard.top - 5
    right = gameboard.left + gameboard.width + 10
    bottom = gameboard.top + gameboard.height + 15
elif side == "B":
    gameboard = gui.locateOnScreen('./img/black/chessboard_black.png', confidence=0.55, grayscale=True)
    left = gameboard.left - 10
    top = gameboard.top - 5
    right = gameboard.left + gameboard.width + 10
    bottom = gameboard.top + gameboard.height + 15

widthInterval = (right - gameboard.left) / 8
heightInterval = (bottom - gameboard.top) / 8

#
# DEFINES A FUNCTION THAT COUNTS THE SCORE 
# - NUMBER OF YOU SIDE AND THEN SUBTRACT THE NUMBER OF OPPOSITE SIDE
#

def Score():
    for i in range(8):
        for j in range(8):
            tempX = 32 + (i * widthInterval)
            tempY = 32 + (j * heightInterval)
            if gui.pixelMatchesColor(tempX, tempY, (87, 83, 82), tolerance=20):
                print("True!")
    
    if side == "W":
        print("White!")
    elif side == "B":
        print("Black!")


Score()