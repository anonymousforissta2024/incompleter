#Source: https://stackoverflow.com/questions/42992240/name-error-in-python-3-6
#!/usr/bin/env python3
import sys; print(sys.version)
import random

##Creates values to use to make random equation.

x = random.randint(1,11)
y = random.randint(1,11)
if x > y:
    total = random.randint(x, 20)
else:
    total = random.randint(y, 20)

##Creates actual values for A,B,C, and D in equation A+B=C+D

a = x
b = total - a
c = y
d = total - y

##Prints option choices and asks for user input

def start_game_message():
    print ("Please fill in the blanks to make the following equation true:")
    print ("__+__=__+__")
    print ("The option choices are:" + str(a) + ", " + str(b) + ", "  + str(c) + ", " + str(d))
def ask_for_input():
    blank1 = input("What is the value of the first blank?")
    blank2 = input("What is the value of the second blank?")
    blank3 = input("What is the value of the third blank?")
    blank4 = input("What is the value of the fourth blank?")
start_game_message()
##Check if user input is correct
def check_answer():
    ask_for_input()
    print (blank1)
    if int(blank1)+ int(blank2) == int(blank3) + int(blank4):
        print ("That is correct!")
    else:
        print ("That is incorrect. Please try again.")
        ask_for_input()
check_answer()