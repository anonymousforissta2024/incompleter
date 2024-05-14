#Source: https://stackoverflow.com/questions/36368878/this-is-the-error-i-get-after-making-the-following-code-typeerror-unorderable
import random
SecretNumber=(random.randint)

Guess=input("Please enter your guess: ")
NumberofGuesses=1

while Guess != SecretNumber:
            NumberofGuesses=NumberofGuesses+1


            if Guess>SecretNumber:
               print("Please insert a smaller number")

            else:
               print("Please insert a bigger number")

print("Number of Guesses: {0}".format(NumberofGuesses))