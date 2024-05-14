#Source: https://stackoverflow.com/questions/47702659/attribute-error-problems-with-python-hangman-code
import random

name = input("Hello, my name is H.A.N.K.M.A.N! What is yours?: ")
print("Hello, "+name," do you wanna play Hangman? Yes? Well why didn't you say so? Lets Goooooooo!")

def extractwords(filename,number):
    myfile=open(filename+".txt","r")
    details=myfile.readlines()
    myfile.close()
    words=[]
    for i in details:
        for item in i.split():
            letter=True
            for j in item:
                if j.isalpha()==False:
                    letter = False
            item = item.lower()
            if len(item)==number and letter==True and item not in words:
                    words.append(item)
    return words
player = "y"
while player =="y":
    complete=0
    guessed=[]
    errors=""
    characters = random.randint(5,9)
    tries = characters+3

    wordlist=extractwords("wordlist",characters)
    word=random.choice(wordlist)
    print("Testing word:",word)
    print("You have "+ str(tries)+" tries left")

    letters=[]
    for i in word:
        letters.append(i)

    hword=[]
    for i in range(0,characters):
        hword.append("-")

    dashes=""
    for i in hword:
        dashes = dashes+i

    print("The word you need to guess is ",dashes)
    while complete < characters and tries > 0:
        guess = input("Please input your letter: ")
        if guess in word:
            guessed.append(dashes)
            print("Noice job! You guessed the right letter!")
            tries=tries-1
            print("You have "+ str(tries)+" tries left")
            print(dashes)
            if len(guessed) == len(word):
                print("What? How did this happen? Yuu must have been cheating!Just Kidding! You did a good job on finding the word, so a GOOD JOB is in order!")
                layer = input("Would you like to play again? y/n: ")
        elif guess.isalpha and guess not in word:
            tries=tries-1
            print("I am sorry, but your guess is a number / not part of the word that I am thinking off. Please have another go!")
            errors.append(guess)
            print("The letters you entered so far:", errors)
            print("You have "+ str(tries)+" tries left")
        elif len(guess)!=1 or "abcdefghiklmnoopqestuvwxyz":
            print("Please enter a valid/single letter.")
        elif guess in guessed:
            print("Please enter a letter that you havent entered previously. ")
        else:
            pass
    if tries==0:
        print("You lose!The word you were supposed to guess was ",word)
player = input("Would you like to play again? y/n: ")