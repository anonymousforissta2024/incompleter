#Source: https://stackoverflow.com/questions/31988132/list-of-words-typeerror-str-does-not-support-the-buffer-interface
# Hangman
#
# -----------------------------------
# Helper code
# List of words - TypeError: 'str' does not support the buffer interface, Python v.3.4


import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

wordlist = load_words()