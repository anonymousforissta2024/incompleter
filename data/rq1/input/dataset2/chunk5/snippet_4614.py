#Source: https://stackoverflow.com/questions/48912755/nameerror-name-guessestaken-is-not-defined-issue
import random

def Loop():

  guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 100)
print('Hi, ' + myName + ', I am thinking of a number between 1 and 100.')

mod = number % 2
if mod > 0:
    print("The number I am thinking of is odd.")
else:
    print("The number I am thinking of is even.")


while guessesTaken < 10:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') 

    if guess > number:
        print('Your guess is too high.')
        if guess == number:
          break

    if guess == number:
        print('Good job, ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
        guessesTaken = 10




if guess != number:
  print('Nope. The number I was thinking of was ' + str(number))

  playagain = input('Would you like to play again')
  if playagain == "yes":
            Loop()
  if playagain == "no":
            print ( 'Goodbye :)')
            Loop()