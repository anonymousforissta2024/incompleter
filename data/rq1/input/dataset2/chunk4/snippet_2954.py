#Source: https://stackoverflow.com/questions/71558427/typeerror-write-argument-must-be-str-not-int-error-continues-to-appear
import winsound
import random
import sys
import time


# Slowtype function


def HandleSounds(SoundToPlay, kplaying):
    if SoundToPlay == 'No':
        return
    else:
        sound2Play = f"./sounds/{SoundToPlay}"
        if kplaying:
            winsound.PlaySound(sound2Play, winsound.SND_ALIAS | winsound.SND_ASYNC)
        else:
            winsound.PlaySound(sound2Play, winsound.SND_ALIAS | winsound.SND_ASYNC)



def slow_type(t, speed):

    HandleSounds("Typing.wav", True)

    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(.1)
        time.sleep(random.random() * 10.0 / speed)
    winsound.PlaySound(None, winsound.SND_ALIAS)
    print('')



# loadMap contains the long descriptions which tell the player where they are and what directions/ actions they have. It also contains the actual map.
# The sound file being played using the playsound module seems to play first before the program runs, just throwing that out there.



def loadMap():
    slow_type("Welcome poor lost soul.", mediumText)

    slow_type("It seems you have been trapped on the grounds of an old estate which has been left to rot and decay within the sands of time.", mediumText)

    slow_type("You have 13 hours to escape, unlock the doors, solve the puzzles and find your way out.", mediumText)

    slow_type("Escape or die trying, the choice is yours.", mediumText)

    slow_type("May the gods be with you...", mediumText)

    R1ld = ("I am in the Parlor, how did I end up in this place? ", mediumText)

    ("Available directions are east.", mediumText)

    R2ld = ("R2 - I am currently in the Grand Library, it seems these books haven't been touched in ages. ", mediumText)

    ("Available directions are north or south.", mediumText)

    R3ld = ("R3 - I made it to the study. There is old paper everywhere. ", mediumText)

    ("Available directions are west or north.", mediumText)

    R4ld = ("R4 -Ah, the old servants quarters. There is an odd looking pedestal in the far corner of the room. ", mediumText)

    ("Move the dials or leave the room: ", mediumText)

    ("Available directions are east or west", mediumText)

    R5ld = ("R5 - I am in the kitchen, it reeks of food, a century past its expiration date. ", mediumText)

    ("Available directions are west or north", mediumText)

    R6ld = ("R6 - This is just a sitting room, There is an odd contraption on the wall. ", mediumText)

    ("Available directions are west or south. ", mediumText)

    ("Enter the time of moonrise and sunset: ", mediumText)

    S7ld = ("R7 - You are now on the second story. ", mediumText)

    ("Available directions are west or north", mediumText)

    H8ld = ("Proceed down the hallway or go down a level? ", mediumText)

    ("Available directions are north or south.", mediumText)

    R9ld = ("You proceeded down the hall to the bathroom. ", mediumText)

    ("Available directions are east or south.", mediumText)

    R10ld = ("Turn around and go into the hall? ", mediumText)

    ("There's a code written on the wall, it reads as follows: 1874 ", mediumText)

    ("Available directions are east or west.", mediumText)

    R11ld = ("You went back into the hall and entered the Porcelain Doll room. The dolls won't stop blinking. ", mediumText)

    ("Available directions are east or west.", mediumText)

    R12ld = ("You exited the Porcelain Doll room and entered the Funeral Parlor/Dining Room. ", mediumText)

    ("Available directions are east or west.", mediumText)

    R13ld = ("You left the Funeral Parlor and proceeded to the Laundry Room. ", mediumText)

    ("Available directions are south or west.", mediumText)

    R14ld = ("You entered the Storage Room. ", mediumText)

    ("Available directions are south or north.", mediumText)

    E15ld = ("Exit the Storage Room? ", mediumText)

    ("Available directions are east or west.", mediumText)

    R16ld = ("You exited the Storage Room. ", mediumText)

    ("Available directions are  south or north.", mediumText)

    S17ld = ("Go upstairs to the Third Floor? ", mediumText)

    ("Available directions are south or east.", mediumText)

    H18ld = ("You went upstairs, you now find yourself on the Third Floor. ", mediumText)
    ("Available directions are north or west.", mediumText)

    R19ld = ("Proceed down the hallway? ", mediumText)

    ("Available directions are south and west.", mediumText)

    R20ld = ("You proceeded down the hall, the stench of mildew is overwhelming. ", mediumText)

    ("Available directions are north or west.", mediumText)

    R21ld = ("You decided to enter the first bedroom, It reeks of rot and mildew. ", mediumText)

    ("Your available directions are south and east.", mediumText)

    R22ld = ("You exited the first bedroom and entered the second bedroom. ", mediumText)
    ("You wrote down a weird combination etched into the plaster of the wall. ", mediumText)

    ("Right 1 time (dial 1), Left 3 times (dial 2), Left 2 times (dial 3), Right 4 times (Dial 4). ", mediumText)

    ("(Hint: Try this combination at the pedestal in the Servants Quarters.) ", mediumText)

    ("Available directions are south or north.", mediumText)

    E23ld = ("Exit the Room? ", mediumText)
    ("Available directions are north or west.", mediumText)

    H24ld = ("You decided to exit the room and headed back into the hallway. ", mediumText)
    ("Available directions are south or east.", mediumText)

    R25ld = ("Enter the Guest Bedroom? ", mediumText)

    ("Available directions are south or east", mediumText)

    R26ld = ("You decided the enter the Guest Bedroom, nothing to see here. ", mediumText)
    ("Just old dusty furniture, not worth sitting on. ", mediumText)

    ("Available directions are south or north.", mediumText)

    R27ld = ("You left the guest bedroom and proceeded down the hall to the Painting Gallery. ", mediumText)
    ("Available directions are south or east", mediumText)

    R28ld = ("You left the Painting Gallery and entered an Empty Bedroom. ", mediumText)
    (" The room is empty, Aside from a set of numbers. ", mediumText)

    ("The numbers represent the moonrise time and the time of sunset: 11:27, 6:12. ", mediumText)

    ("These numbers could be a clue to the weird lock contraption in the sitting room on the main floor. ", mediumText)

    ("You can go either north or east.", mediumText)

    S29ld = ("Go upstairs? ", mediumText)
    ("Available directions are south or west.", mediumText)

    H30ld = ("You are now in the 4th floor hallway. You can go north or west.", mediumText)

    R31ld = ("You left the hallway and entered the first room you could open. ", mediumText)
    ("You entered the Sitting Room, Maybe you should take a rest. ", mediumText)

    ("You can go either east or west.", mediumText)

    R32ld = ("You left the confines of the Sitting Room and entered the Smoking Room. ", mediumText)
    ("It smells like old cigars.", mediumText)

    ("You can go south or east", mediumText)

    R33ld = ("You left the Smoking Room and entered the Game Room", mediumText)
    (" You can go either south or west.", mediumText)

    R34ld = ("You left the Game Room and opened the Master Bedroom. ", mediumText)
    ("There is another weird puzzle", mediumText)

    ("Your available directions are south or east. ", mediumText)

    R35ld = ("You left the Master Bedroom and entered the Balcony. The moon is full. ", mediumText)
    ("Directions are south & east.", mediumText)

    R36ld = ("You left the Balcony and went back to the Parlor. ", mediumText)
    ("You can now leave the manor, proceed? ", mediumText)

    ("Please enter the code to escape: ", mediumText)



    # Manor Floor plan
    manorMap = {"R1": {"LocDesc": R1ld, "e": "R2", "w": "No", "n": "No", "s": "No", "lock": "No", "count": 0},

                "R2": {"LocDesc": R2ld, "e": "No", "w": "No", "n": "R1", "s": "R3", "puzzle": "No", "count": 0, "lock": "No"},

                "R3": {"LocDesc": R3ld, "e": "No", "w": "R2", "n": "R4", "s": "No", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R4": {"LocDesc": R4ld, "e": "R5", "w": "R3", "n": "No", "s": "No", "puzzle": "Rewire",
                       "solution": "Rewire", "lock": "No",
                       "count": 0},

                "R5": {"LocDesc": R5ld, "e": "No", "w": "R4", "n": "R6", "s": "No", "puzzle": "No",
                       "lock": "No",
                       "count": 0},

                "R6": {"LocDesc": R6ld, "e": "No", "w": "R5", "n": "No", "s": "R7", "Lock": "The Sun & The Moon",
                       "Puzzle": "No", "count": 0},

                "R7": {"LocDesc": S7ld, "e": "No", "w": "R6", "n": "R8", "s": "No", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R8": {"LocDesc": H8ld, "e": "No", "w": "No", "n": "R9", "s": "R7", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R9": {"LocDesc": R9ld, "e": "R10", "w": "No", "s": "R8", "n": "No", "puzzle": "No", "lock": "No",
                       "count": 0},

                "R10": {"LocDesc": R10ld, "e": "R11", "w": "R9", "s": "No", "n": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R11": {"LocDesc": R11ld, "e": "R12", "w": "R10", "s": "No", "n": "No", "lock": "No", "puzzle": "No",
                        "count": 0},

                "R12": {"LocDesc": R12ld, "e": "R13", "w": "R11", "s": "No", "n": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R13": {"LocDesc": R13ld, "s": "R12", "n": "No", "e": "No", "w": "R14", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R14": {"LocDesc": R14ld, "s": "R15", "n": "R13", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R15": {"LocDesc": E15ld, "s": "No", "n": "No", "e": "R14", "w": "R16", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R16": {"LocDesc": R16ld, "s": "R15", "n": "R17", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R17": {"LocDesc": S17ld, "s": "R16", "n": "No", "e": "R18", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R18": {"LocDesc": H18ld, "s": "No", "n": "R17", "e": "No", "w": "R19", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R19": {"LocDesc": R19ld, "s": "R20", "n": "No", "e": "No", "w": "R18", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R20": {"LocDesc": R20ld, "s": "No", "n": "R19", "e": "No", "w": "R21", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R21": {"LocDesc": R21ld, "s": "R22", "n": "No", "e": "R20", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R22": {"LocDesc": R22ld, "s": "R23", "n": "R21", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "E23": {"LocDesc": E23ld, "s": "No", "n": "R22", "e": "No", "w": "R24", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R24": {"LocDesc": H24ld, "s": "R25", "n": "No", "e": "R23", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R25": {"LocDesc": R25ld, "s": "R24", "n": "No", "e": "R26", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R26": {"LocDesc": R26ld, "s": "R27", "n": "R25", "e": "No", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R27": {"LocDesc": R27ld, "s": "R28", "n": "No", "e": "No", "w": "R26", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R28": {"LocDesc": R28ld, "s": "No", "n": "R27", "e": "R29", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R29": {"LocDesc": S29ld, "s": "R28", "n": "No", "e": "No", "w": "R30", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R30": {"LocDesc": H30ld, "s": "No", "n": "R31", "e": "No", "w": "R29", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R31": {"LocDesc": R31ld, "s": "No", "n": "No", "e": "R32", "w": "R30", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R32": {"LocDesc": R32ld, "s": "R33", "n": "No", "e": "R31", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R33": {"LocDesc": R33ld, "s": "R34", "n": "No", "e": "No", "w": "R32", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R34": {"LocDesc": R34ld, "s": "R35", "n": "No", "e": "R33", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R35": {"LocDesc": R35ld, "s": "R36", "n": "No", "e": "R34", "w": "No", "puzzle": "No", "lock": "No",
                        "count": 0},

                "R36": {"LocDesc": R36ld, "s": "No", "n": "R1", "e": "No", "w": "R35", "puzzle": "No", "lock": "No",
                        "count": 0}}

    return manorMap


def checkDirection(direction, currLock):
    LowerD = direction.casefold()
    newSpot = currLock.get(LowerD)

    # print(newSpot)
    if newSpot != "No":

        return newSpot

    else:

        return None



slowText = 60
mediumText = 200
fastText = 300
superSlowText = 25



maplist = loadMap()

startLoc = "R1"

prePlayerLoc = startLoc

playerLoc = startLoc

keepPlaying = True


'''def HandleLock1():
    if solvePuzzle == "R36" and input(prompt).isnumeric() == "1874":

        if input(prompt) == "1874":
            print("You Escaped, congratulations! (type q to exit.)")

    if solvePuzzle == "R6" and input(prompt).isnumeric() == "11:27, 6:12":

        if input(prompt) == "11:27" "6:12":
            print("password accepted")'''



'''def HandlePuzzle2():
    if solvePuzzle == "R34" and input(prompt).islower() == "eternity":

        if input(prompt) == "eternity":
            print("Password excepted.")

    if solvePuzzle == "R4" and input(prompt).isupper() == "Right , Left , Left, Right":

        if input(prompt) == "Right , Left , Left, Right":
            print("Puzzle Complete!")'''



while keepPlaying:

    currLoc = maplist.get(playerLoc)

    lockName = currLoc.get("lock")

    puzzleName = currLoc.get("puzzle")

    currLoc["count"] += 1

    print(f"Lock : {lockName} and Puzzle : {puzzleName}")

    '''HandleSounds("rain_thunder.mp3", True)'''

    slow_type(currLoc.get('LocDesc'), mediumText)

    prompt = "\n" + "Lost Soul" + ", What will be your next action? : " + ", Make your choice wisely: "

    playerAction = input(prompt)

    prevPlayerLoc = currLoc

    if playerAction.lower() == "q":
        keepPlaying = False

    else:

        newLoc = checkDirection(playerAction.lower(), currLoc)

        if playerLoc is not None:

            playerLoc = newLoc

        else:
            print("This action cannot be completed! Carry on!")