#Source: https://stackoverflow.com/questions/28253282/python-3-typeerror-type-str-doesnt-support-the-buffer-api
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'rb', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for x in secretWord :
        if x not in lettersGuessed :
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    guessedWord=['_']*len(secretWord)
    for x in lettersGuessed :
##      1**   find the occurences of x in secretWord
        occurences = []
        for i, j in enumerate(secretWord):
             if j == x:
                occurences.append(i)
##      2* go to the same indices in guessedWord and replace them by x 
        for i in occurences :
            guessedWord[i]=x;

    return ''.join(guessedWord)



def getAvailableLetters(lettersGuessed):

    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    available_Letters=[]
    all_letters=list(string.ascii_lowercase)
    for x in all_letters :
         if (x not in lettersGuessed):
             available_Letters.append(x)
    return ''.join(available_Letters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print(" Welcome to the game, Hangman!")
    print("I am thinking of a word that is 4 letters long.")
    number_of_guesses = 8
    lettersGuessed = []
    while True :
        print("--------------------------------")
        print ("You have " , number_of_guesses , "left !")
        print("Available letters : " , getAvailableLetters(lettersGuessed) )
        print("Please guess a letter : ")
        guess = input()

        while True:
                print("Please guess a letter : ")
                if guess in lettersGuessed:
                    print("Oops ! you've already guessed that letter :" , getGuessedWord(secretWord, lettersGuessed))
                    break 
                else :
                    if(guess in secretWord ) :
                        lettersGuessed.append(guess)
                        print("Good guess:", getGuessedWord(secretWord, lettersGuessed) )
                    else :
                        number_of_guesses-=1


        print("---------------------------------")
        if(number_of_guesses == 0) :
            print(" Sorry, you ran out of guesses. The word was else. ")
            break
        if(isWordGuessed(secretWord, lettersGuessed)):
            print(" Congratulations, you won!")
            break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)