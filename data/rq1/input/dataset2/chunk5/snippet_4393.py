#Source: https://stackoverflow.com/questions/61198226/problem-in-pycharm-hangman-game-beginner-here-obviously-typeerror-object-of
# HANGMAN

import random
import time

hangman_pics = ['+-------+\n'
                '|       |\n'
                '        |\n'
                '        |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '        |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '|       |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '|\      |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '/|\     |\n'
                '        |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '/|\     |\n'
                '/       |\n'
                '        |\n'
                '===========]',
                '+-------+\n'
                '|       |\n'
                'O       |\n'
                '/|\     |\n'
                '/\      |\n'
                '        |\n'
                '===========]\n'

                ]

words = [
    "king",
    "fang",
    "long",
    "fast",
    "girl",
    "cats",
    "free",
    "bird",
    "band",
    "skin",
    "pour",
    "smart",
    "games",
    "perch",
    "clamp",
    "clock",
    "photo",
    "friar",
    "flute",
    "first",
    "candy",
    "mouth",
]

win = False
guesses = []


def get_word():
    word = random.choice(words)
    return word


def hidden_word(word, guesses):
    blanks = ''
    for i in word:
        blanks += f'{i} ' if i in guesses else '_ '
    return blanks


def get_guess():
    global guess
    guess = input('\nYour guess: ').lower
    print(len(guess))
    if len(guess) != 1:
        print(f'\n{"- - - - - " * 2}\nOnly guess one letter!\n{"- - - - - " * 2}\n')
    elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
        print(f'\n{"- - - - - " * 2}\nOnly guess letters!\n{"- - - - - " * 2}\n')
    elif guess in guesses:
        print(f'\n{"- - - - - " * 2}\nYou already guessed that, idiot.\n{"- - - - - " * 2}\n')
    else:
        return guess
    guesses.append(guess)


def correct_guess():
    global lives_lost
    lives_lost = 0
    while True:
        if get_guess() in guesses:
            print(f'\n{"- - - - - - " * 2}\nNice, {guess} is in the word.\n{"- - - - - - " * 2}\n')
        elif guess not in word.lower():
            lives_lost += 1
            print(f'\n{"- - - - " * 2}\n"{guess}" is not in the word.\n{"- - - - " * 2}\n')


def display_pic():
    print(hangman_pics[lives_lost])
    print(hidden_word(word, guesses))


def win_or_not():
    win = all(item in guesses for item in list(word))
    return win


while True:
    lives_lost = 0
    word = get_word()
    print(f'\n\nGuess a letter. You have 6 lives. You lose a life every time you guess wrong.\n\n{"-----" * 10} '
          f'\nThis word has {len(word)} letters. \n{"-----" * 10}\n')
    display_pic()
    while True:
        get_guess()
        print(guess)
        correct_guess()
        display_pic()
        if win_or_not() is True:
            print(f'\n{"- - - - - " * 4}\ngood job you won. the word is "{word}".\n{"- - - - - " * 4}')
            break
        elif lives_lost == 5 and win_or_not() is False:
            print(f'\n{"- - - - - " * 2}\nYOU LOSE. the word was "{word}"\n{"- - - - - " * 2}')
            break