#Source: https://stackoverflow.com/questions/36190476/attributeerror-nonetype-object-has-no-attribute-title
import time
import sys

print("Welcome to my quiz")
time.sleep(2)
input('Press enter to continue')

score = int(0)
failed = int(0)

def points():
    print("Correct! Well done!")
    global score
    score = score + 1

def fail():
    print("Oh no, that is incorrect")
    global failed
    failed = failed + 1

def printtotal():
    global score
    global failed
    print("You have ",score,"points, and ",failed,"/3 lives used.")

if failed == 5:
    sys.exit('Program terminated.')

print('You will have 5 seconds to answer each question \nIf you fail 5 times or more, the program will exit')
time.sleep(3)
print('Good luck!')
time.sleep(2)

q1 = print(input("What is the capital of England?")).title
if q1 == 'London':
    points()
else:
    fail()
printtotal()

q2 = print(input("Who is the prime minister's wife?")).title
if q2 == 'Samantha' or 'Samantha Cameron':
    points()
else: 
   fail()
printtotal()

print('How would you say \'I came, I saw, I conquered\' in latin?')
print('a) veni, vidi, vici')
print('b) veni, vedi, vici')
print('c) vini, vedi, vici')
q3 = print(input('Type the letter here:'))
if q3 == 'a)' or 'a':
    points()
else:
    fail()
printtotal()