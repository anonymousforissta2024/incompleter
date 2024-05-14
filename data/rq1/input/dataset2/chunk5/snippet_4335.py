#Source: https://stackoverflow.com/questions/64532267/typeerror-init-missing-4-required-positional-arguments
#! usr/bin/python
import time
import random

print("HI WELCOME TO HANGMAN !")
print("\n")
time.sleep(1.5)
name = input("Enter your name :")
print("\n")
print("HEY " + name + " HOPE YOU HAVE A GOOD TIME PLAYING HANGMAN TODAY")
print("\n")
time.sleep(1.5)
print("YOUR GAME IS ABOUT TO BEGIN IN A FEW SECONDS")
time.sleep(1)


class Hangman():
    def __init__(self, word, guesses, count, limit) :
        self.count = count
        self.display= "_" * self.length 
        self.word = word 
        self.length = len(word)
        self.guessed = []
        self.guesses = guesses
        self.Continue = ""
        self.limit = limit

    def get_word(self):
        words = ["book" ,"paper", "computer", "movie", "mouse", "laptop", "national"]
        self.word = random.choice(words)
    
    def play_loop(self):
        self.Continue = input("Do you wish to play another round? y = yes, n = no")
        if self.Continue == 'y':
            Hangman()
        elif self.Continue == "n":
            print("thanks for playing! hope you had a good time :)")
            exit()

    def play(self,guesses):
        self.count = 5
        print("your word is " + self.word + "enter your guesses ")
        self.guesses = guesses.strip()
        if len(guesses.strip()) == 0:
            print("Invalid input, please enter a letter \n")
        elif len(guesses.strip()) >=2:
            print("Invalid input, please enter one letter at a time \n")

        elif self.guesses in self.word :
            self.guessed.extend(self.guesses)
            self.index = self.word.find(self.guesses)
            self.word = self.word[self.index] + '_' + self.word[self.index + 1]
            self.display = self.display[:self.index] + self.guesses + self.display[:self.index + 1]
            print(self.display + "\n")

        else:
            self.count +=1

        if self.count == 1:
            time.sleep(1)
            print("   _____ \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "__|__\n")
            print(" wrong guess,you have" + str(self.limit - self.count) + "guesses remaining")
        
        elif self.count == 2:
            time.sleep(1)
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print("wrong guess, you have " + str(self.limit - self.count) + "guesses remaining")

        elif self.count == 3:
            time.sleep(1)
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print("wrong guess, you have") + str(self.limit - self.count) + "guesses remaining"

        elif self.count == 4:
            time.sleep(1)
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

        elif self.count == 5:
            time.sleep(1)
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")
            print("wrong guesses, you are hanged!")
            print("the word was" , self.word)
            Hangman.play_loop()

        if self.display:
            print("congrats you won !")
            Hangman.play_loop()
        elif self.count != self.limit:
            Hangman.play_loop()

Hangman_game = Hangman()
Hangman_game()   
        