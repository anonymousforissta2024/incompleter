#Source: https://stackoverflow.com/questions/44179168/typeerror-cant-convert-int-object-to-str-implicitly-when-trying-to-print-a
# Imports
import sys
import os

# Main Vars
gmName = "TXT Adventure"
gmFileName = "txtAdventure"
gmVersion = "2.5.0"
gmSplit = "--------"

# Player Vars
plHealth = 100
plHealthO = 100 # Original Health
plName = "N/A"

# Character Vars
ch1 = "Tom"
ch2 = "Josh"
ch3 = "Demitrie"

# Enemy Vars - en<num>H = heath of enemy
en1 = "Sand Viper"
en1H = "5"
en2 = "Water Venom Moth"
en2H = "7"
en3 = "Giant Ant"
en3H = "10"

# Game
print("Finished Loading!")
print(gmSplit)
cont = input("Press Enter To Continue..")
print(gmSplit)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Space from loading screen
print("Welcome to " + gmName + "!")
print("You are playing on version: " + gmVersion)
print(gmSplit)
plName = input("Who are you, son?\n--> ")
if plName == "":
    exit = input("Invalid Name, Press enter to restart.. ")
    os.startfile(gmName + '.py')
    sys.exit(0)
if plName == " ":
    exit = input("Invalid Name, Press enter to restart.. ")
    os.startfile(gmName + '.py')
    sys.exit(0)
cont = input("Press Enter to continue, " + plName + "!")
print(gmSplit)
print(ch1 + ": Well hello, " + plName + ". Nice to see you!")
cont = input("Press Enter to continue, " + plName + "!")
print(gmSplit)
option = input("What do you want to do?\n1 = Play\n2 = Exit\n--> ")
if option == "1":
    cont = input("Press Enter to continue, " + plName + "!")
    print(gmSplit)
    plAge = input("What is your age, " + plName + "?" + "\n--> ")
    print(gmSplit)
    option2 = input("So you are " + plName + " and you are " + plAge + " years old?\n1 = True\n2 = False\n--> ")
    if option2 == "1":

        # Start of the game
        print(gmSplit)
        print("Well welcome to " + gmName + ", " + plName + "!")
        print(gmSplit)
        start = input("Press Enter To Start The Game..")
        print(gmSplit)
        print(ch1 + ": Hi there traveler, we are from far away lands!")
        cont = input("Press Enter To Continue..")
        print(gmSplit)
        print(ch2 + ": Like the scally said, we' came from a long way away ay!")
        cont = input("Press Enter To Continue..")
        print(gmSplit)
        print(ch1 + " + " + ch2 + ": I WILL KILL UUU!")
        cont = input("Press Enter To Continue..")
        print(gmSplit)
        option = input(ch3 + ": Break it up you to! Don't you think, " + plName + "!\n1 = True\n2 = False\n--> ")
        if option == "1":
            print(ch3 + ": Well thank you, " + plName + ".")
            print(ch1 + " + " + ch2 + ": Ugh...")
            print(gmSplit)
        else:
            print(ch3 + ": Oh, i'm sorry, did I upset you..")
            cont = input("Press Enter To Continue..")
            print(gmSplit)
        print(ch3 + ": Well anyway, they are still fighting..")
        print(ch1 + " + " + ch2 + ": ARAGHHH!")
        print(gmSplit)
        cont = input("Press Enter To Continue..")
        print(gmSplit)
        print(ch1 + " + " + ch2 + " + " + ch3 + ": Okay lets start the adventure!")
        cont = input("Press Enter To Continue..")
        way = input(ch1 + ": Okay, " + plName + ". What way are we going?\n1 = North\n2 = South\n--> ")
        if way == "1":
            print(ch1 + ": Okay, lets go north!")
        elif way == "2":
            print(ch1 + ": Okay, lets go south!")
            print(gmSplit)
            cont = input("Press Enter To Continue..")
            print(gmSplit)
            print(ch3 + ": But I dont like going south, it's scary that way..")
            print(gmSplit)
            cont = input("Press Enter To Continue..")
            print(gmSplit)
            print(ch1 + " + " + ch2 + ": Shut up, " + ch3 + "!")
            print(ch3 + ": Please don't go this way, " + plName + " :(")
            option = input("1 = Continue South\n2 = Go North insted\n--> ")
            if option == "1":
                plHealth -= 5
                print(gmSplit)
                print(ch3 + ": Why, " + plName + ". Why did you do this!")
                print(gmSplit)
                print("*" + ch3 + " slaps you, your health goes from " + plHealthO + " to: " + plHealth + "!")
        else:
            print("You picked an invalid choice!")
            exit = input("Press enter to re-do choice!")
        print(gmSplit)
        print("You have encounterd a wild: " + en1 + "! It has " + en1H + " health!")
        option = input("What do you want to do?\n1 = Attack\n2 = Run\n--> ")
        if option == "1":
            en1H = "3"
            plHealth -= 2
            print("The " + en1 + "'s health has gone down to: " + en1H + "!")
            cont = input("Press Enter To Continue..")
            print(gmSplit)
            print("The " + en1 + " attacked you!")
            cont = input("Press Enter To Continue..")
            print(gmSplit)
            print("Your health was: " + plHealthO + "But now it has gone down to: " + plHealth + "!")
            cont = input("Press Enter To Continue..")
            print(gmSplit)
            print(ch1 + " + " + ch2 + " Helped  you and killed the beast!")
            cont = input("Press Enter To Continue..")
            print(gmSplit)
            print("Okay, where do you want to go now?")
            option = input("1 = Keep Heading Forward\n2 = Camp for the night\n--> ")
        elif option == "2":
            exit = input(en1)
        else:
            print("You chose an invalid choice!")
            print(gmSplit)
            restart = input("Press enter to restart..")
            os.startfile(gmFileName + '.py')
            sys.exit(0)
    elif option2 == "2":
        exit = input("Press enter to restart.. ")
        os.startfile(gmFileName + '.py')
        sys.exit(0)
    else:
        exit = input("Press enter to restart.. ")
        os.startfile(gmFileName + '.py')
        sys.exit(0)
elif option == "2":
        exit = input("Press enter to exit " + gmName + ".. ")
        os.startfile(gmFileName + '.py')
        sys.exit(0)
else:
        exit = input("Press enter to restart.. ")
        os.startfile(gmFileName + '.py')
        sys.exit(0)