#Source: https://stackoverflow.com/questions/37003943/previous-function-does-not-carry-over-to-next-function-nameerror-name-is-not-de
import random

def setup():

    print("Reading Word List...")
    print("Selecting Secret Word...")
    print("A secret word has been selected...")

setup()

def loadwordlist():

    word = open ('words.txt').read().splitlines()
    secret_word = random.choice(word).lower()
    guessed_word = []
    guessed_letters = []
    for letters in secret_word:
        guessed_word.append('_')
    return ' '.join(guessed_word)

print(loadwordlist())

total_guesses = 10
print(("You have {} guesses left").format(total_guesses))

def gethint():

    loadwordlist()
    guess = input("Please enter a guess:")
    guess = guess.lower()
    if guess in guessed_word:
        print("You guessed Correctly")
        guessed_letters.append(guess)

gethint()