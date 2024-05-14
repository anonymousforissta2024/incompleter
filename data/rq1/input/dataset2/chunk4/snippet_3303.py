#Source: https://stackoverflow.com/questions/47373427/typeerror-function-object-is-not-subscriptable-on-a-string
import random

def num():
    """Returns a number between 1000 and 9999."""
    num = str(random.randint(1000, 9999))
    print("Random number is: " + num) #for testing purposes
    return num

def userNum():
    """Asks user for a number between 1000 and 9999."""
    while True:
        try:
            userNum = int(input("Choose a number between 1000 and 9999: "))
        except ValueError:
            print("This isn't a number, try again.")
            continue
        if userNum < 1000 or userNum > 9990:
            print("Your number isn't between 1000 and 9999, try again.")
            continue
        else:
            break
    userNum = str(userNum)
    return userNum

def numCheck(num, userNum):
    """Checks the number of cows and bulls."""
    cow = 0
    bull = 0
    for i in range(0, 3):
        if userNum[i] == num[i]:
            cow += 1
        else:
            bull += 1
    print("You have " + str(cow) + " cow(s) and you have " + str(bull) + " bull(s).")
    return cow

def gameLoop():
    """Loops the game until the user find the right number."""
    num()
    cow = 0
    if cow < 4:
        userNum()
        numCheck(num, userNum)
    else:
        print("Congratulation, You found the right number!")

gameLoop()