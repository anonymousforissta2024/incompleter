#Source: https://stackoverflow.com/questions/44230925/python-typeerror-unhashable-type-image
import time
import pyautogui

#option = None

def main():
    #find_notification()
    name_coords, reply_coords, text_coords = set_message_coords()
    option = read_message(text_coords)
    player_id(name_coords, option)
    answer = response()
    reply(reply_coords, answer)


def find_notification(): #looks for a waiting PM and clicks it
    while True:
        image = pyautogui.locateCenterOnScreen('test.png', grayscale = False, confidence = .9)
        print(image)
        if image is not None:
            print('Found a waiting message')
            pyautogui.click(image)
            break


def set_message_coords(): # Creates coords for message box and screenshots name
    try:
        imagex, imagey = pyautogui.locateCenterOnScreen('upper_right_message_corner.png', grayscale = True, confidence = .8)

    except:
        print('ERROR I SHOULD BE FINDING "upper_right_message_corner.PNG" EXITING PROGRAM') 
        exit()
    name_coords = (imagex - 424), imagey, 378, 50 # The coords of where the players name would be
    print('Found an open message')
    print(imagex, imagey)

    reply_coords = (imagex - 251), (imagey + 255 ) # Coords of the reply button
    text_coords = (imagex - 461), (imagey + 45), 430, 45 # Coords of where a players possible response is
    return name_coords, reply_coords, text_coords # Returns all coord values to be used by other functions


def player_id(name_coords, option): # Indentifies person who messaged and depending on if this person has messaged before changes response
    players = {} # Used to store players names and where in the response is

    name_image = pyautogui.screenshot('name_test.png', region = name_coords) # Names are screenshots 

    if name_image not in players:
        print("User was not previously found, adding to dictionary.")
        players[name_image] = None
    else:
        print("User is previous user.")
        players[name_image] = players[name_image] + option
        return players[name_image]


def reply(reply_coords, response): #Replies to PM
    pyautogui.click(reply_coords)
    pyautogui.typewrite(response)
    pyautogui.press('enter')


def read_message(text_coords): # Reads PM for numbers and sets option the number
    if pyautogui.locateCenterOnScreen('1.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '1'
    elif pyautogui.locateCenterOnScreen('2.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '2'
    elif pyautogui.locateCenterOnScreen('3.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '3'
    elif pyautogui.locateCenterOnScreen('4.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '4'
    elif pyautogui.locateCenterOnScreen('5.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '5'
    elif pyautogui.locateCenterOnScreen('6.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '6'
    elif pyautogui.locateCenterOnScreen('7.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '7'
    elif pyautogui.locateCenterOnScreen('8.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '8'
    elif pyautogui.locateCenterOnScreen('9.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '9'
    elif pyautogui.locateCenterOnScreen('0.png',region = text_coords,  confidence = .9, grayscale = True):
        option = '0'
    else:
        print('ERROR CANT FIND DIGIT ANSWER')
        option = None
        #reply(reply_coords,'ERROR PLEASE ENTER A NUMBER RESPONSE!')
        #main()
    print(option)
    return option


def response(option): # All the possible responses the bot can give a player
    if option == None:
        return "Hello! I am bot made to answer your questions! PM the number for more options! 1: Bounties. 2: Bug Hunting. 3: Looting. 4: Farming."
    elif option == '1':
        return "The bounty quest allows you to hunt mobs for cash! Location: Castle, steward's room(to the right in the throne room) [PM 1 for specifics, PM 2 for TIPS, PM 3 for possible bounties]"
    elif option == '12':
        return '1. The bounty box will "drop"(stop following you, and will not pick up anything) after every kill/capture you get, and will require you to call it, or run over it to pick it up again. [PM 1 for more info, PM 9 to go back one level, PM 0 to reset choices]'
    elif option == '13':
        return '100 green blobs, 20 Lizardons, 75 Pyrats(as homage to the PQ I assume), 75 Rebel soldiers(regular green baddy), 60 dark blobs, 60 rats, 75 snakes, 75 bats, 75 bandits, 80 spiders, 50 archers, or 50 crabs. [PM 9 to go back one level, PM 0 to reset choices]'

main()