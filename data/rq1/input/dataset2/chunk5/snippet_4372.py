#Source: https://stackoverflow.com/questions/72299517/typeerror-in-python-in-custom-input-function-exception-handling
import random
randInt = random.randint(1, 100)
count = 1
print("RandInt: " + str(randInt))


def takeInput(message):
    userInput = input(message)
    try:
        userInput = int(userInput)
        print("takeInput try " + str(userInput)) #This line is printing correct value every time
        return userInput
    except ValueError as e:
        takeInput("Not a valid number, try again: ")


userInput = takeInput("Please enter a number: ")

while(not(userInput == randInt)):
    print("while loop " + str(userInput)) #I am receiving a none value after I raise an exception and then enter a valid number
    if(userInput < randInt):
        userInput = takeInput("Too small, try again : ")
    else:
        userInput = takeInput("Too large, try again : ")
    count += 1

print("Congratulations, you guessed it right in " + str(count) + " tries.")