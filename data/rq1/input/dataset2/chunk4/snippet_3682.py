#Source: https://stackoverflow.com/questions/34245525/typeerror-when-user-cancels-input-dialog
""" A simple typing program

Press "H" to draw an H
Press "E" to draw an E
Press "L" to draw a L
Press "O" to draw an O
Press "W" to draw a W
Press "R" to draw a R
Press "D" to draw a D
Press "ENTER" to go to the next line
Press "TAB" to make an indent
Press "BACKSPACE" to go backwards an indent
Press the "Up" or "Down" arrow keys to move the turtle up or down the canvas
Press "SPACE" to clear the canvas of your drawings
Press "ESC" to exit the program
Press any number from 1-0 on the key board (1 = 1, 0 = 10) to set the letter thickness
Press any key from F1-F10 to set a random color of the letter
(F1-F8 = colors, F9 = Custom Color, F10 = Original color)

That is all you need to know! Enjoy! """

from turtle import *
from tkinter import *
import math
from tkinter.colorchooser import *
import copy

# Function variables

space_width = 30 # Default value: 30
letter_height = 100 # Default value: 100
letter_width = 50 # Default value: 50



change = (input("Would you like to change the size of the letters from the defult value? y/any other input: "))

y = ("yes")
n = ("no")


if change in y:
    try:
        while True:
            try:
                letter_height = int(input("Enter a value from 1-170 to set the height of each letter in pixels: "))
                break
            except ValueError:
                print("That is not an integer! Please enter an integer from 1-170!")
        while letter_height > 170:
            try:
                letter_height = int(input("That value is too much. Please reenter a value from 1-170: "))
                while letter_height < 1:
                    letter_height = int(input("That value is too little. Please reenter a value from 1-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 1-170!")
        while letter_height < 1:
            try:
                letter_height = int(input("That value is too little. Please reenter a value from 1-170: "))
                while letter_height > 170:
                    letter_height = int(input("That value is too much. Please reenter a value from 1-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 1-170!")
        while True:
            try:
                letter_width = int(input("Enter a value from 1-170 to set the width of each letter in pixels: "))
                break
            except ValueError:
                print("That is not an integer! Please enter an integer from 1-170!")
        while letter_width > 170:
            try:
                letter_width = int(input("That value is too much. Please reenter a value from 1-170: "))
                while letter_width < 1:
                    letter_width = int(input("That value is too little. Please reenter a value from 1-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 1-170!")
        while letter_width < 1:
            try:
                letter_width = int(input("That value is too little. Please reenter a value from 1-170: "))
                while letter_width > 170:
                    letter_width = int(input("That value is too much. Please reenter a value from 1-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 1-170!")
            break
    except:
        input("That is not an answer! Please enter either y or n!: ")

elif change in n:
    space_width = 30 # Default value: 30
    letter_height = 100 # Default value: 100
    letter_width = 50 # Default value: 50

#The 'while' loop below will tell the user to choose a color name, but if the color is invalid, an exception is thrown, and the user must reenter a color name until a valid color name is entered. 

while True:
    try:
        pen_color=input("Enter a color name to set the pen color: ")
        pencolor(pen_color)
        break
    except:
        print("That is either not an available color or not a valid color name. Please reenter the name of another color or a valid one.")

def NewLetterDimensions():
    global letter_height
    letter_height = (numinput("New Letter Height", "Please set the new letter height: ", minval = 10, maxval = 170))

    global letter_width
    letter_width = (numinput("New Letter Width", "Please set the new letter width: ", minval = 10, maxval = 170))

    penup()
    goto(xcor(), ycor() +letter_height)
    pendown()
    listen()

def draw_space():
    # Add a space 30 pixels wide.
    penup()
    forward(space_width)
    pendown()

def move_turtle():
    # Pick up the turtle and move it to its starting location.
    penup()
    goto(-200, 100)
    pendown()

def draw_H():
    # Draw the left leg of H.
    # The turtle starts at the bottom left of the letter, pointing right.
    left(90)
    forward(letter_height)
    # Draw the bar of the H.
    # The turtle starts at the top of the left leg, pointing up.
    forward(-letter_height/2)
    right(90)
    forward(letter_width)
    # Draw the right leg of the H.
    # The turtle starts at the right side of the bar, pointing right.
    left(90)
    forward(letter_height/2)
    forward(-letter_height)
    right(90)
    # The H is drawn.
    # The turtle is in the top right, pointing right.
    draw_space()


def draw_E():
    # Draw an E.
    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    forward(-letter_width)
    right(90)
    forward(letter_height/2)
    left(90)
    forward(letter_width)
    forward(-letter_width)
    right(90)
    forward(letter_height/2)
    left(90)
    forward(letter_width)
    draw_space()

def draw_L():
    # Draw an L
    left(90)
    forward(letter_height)
    forward(-letter_height)
    right(90)
    forward(letter_width)
    draw_space()

def draw_O():
    # Draw an O
    forward(letter_width)
    left(90)
    forward(letter_height)
    left(90)
    forward(letter_width)
    left(90)
    forward(letter_height)
    left(90)
    forward(letter_width)
    draw_space()

def draw_newline():
    # This funtion will pick up the turtle and move it to a second line below HELLO
    penup()
    goto(xcor(), ycor() -letter_height-5)
    pendown()

def draw_W():
    # This function will draw a W
    left(105)
    forward(letter_height)
    backward(letter_height)
    right(40)
    forward(letter_height/2)
    right(131)
    forward(letter_height/2)
    left(141)
    forward(letter_height)
    right(165)
    penup()
    forward(letter_height)
    left(90)
    draw_space()

def draw_second_O():
    # This function will draw the O in "world"
    forward(letter_width)
    right(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    right(90)
    forward(letter_height)
    right(90)
    penup()
    forward(letter_width)
    right(90)
    forward(letter_height)
    left(90)
    draw_space()

def draw_R(letter_width, letter_height):
    # This function will draw an R

    slant_height = (math.sqrt(letter_width**2 + (letter_height/2)**2))
    slant_angle = (90+(90-(math.degrees(math.acos(letter_width/slant_height)))))
    space_angle = (180 - slant_angle)

    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    right(90)
    forward(letter_height/2)
    right(90)
    forward(letter_width)
    left(slant_angle)
    forward(slant_height)
    left(space_angle)
    draw_space()

def draw_D(letter_width, letter_height):
    # This function will draw a REAL D

    angle_height = math.sqrt(letter_width**2 + (letter_height/2)**2)
    D_angle = (90+(math.degrees(math.acos(letter_width/angle_height))))
    Second_D_angle = ((90 - (D_angle-90)) + (90-(math.degrees(math.acos(letter_width/angle_height)))))
    D_space_angle = (math.degrees(math.atan(letter_width/(letter_height/2))))

    left(90)
    forward(letter_height)
    right(D_angle)
    forward(angle_height)
    right(Second_D_angle)
    forward(angle_height)
    left(90+D_space_angle)
    penup()
    forward(letter_width)
    draw_space()

def skip(x, y):
    penup()
    goto(x, y)
    pendown()

def back():
    penup()
    bk(letter_width + space_width)
    pendown()

def walk():
    penup()
    forward(letter_width + space_width)
    pendown()

def soar():
    penup()
    left(90)
    forward(letter_height + 5)
    right(90)
    pendown()

def fall():
    penup()
    right(90)
    forward(letter_height + 5)
    left(90)
    pendown()

setup(1.0, 1.0)

def RotateRight():
    right(90)

def RotateLeft():
    left(90)

def Up():
    penup()
    goto(xcor(),ycor()+(letter_height+5))
    pendown()

def width1():
    width(1)

def width2():
    width(2)

def width3():
    width(3)

def width4():
    width(4)

def width5():
    width(5)

def width6():
    width(6)

def width7():
    width(7)

def width8():
    width(8)

def width9():
    width(9)

def width10():
    width(10)

def Blue():
    color("blue")

def Red():
    color("red")

def DarkGreen():
    color("dark green")

def Purple():
    color("purple")

def Pink():
    color("pink")

def Brown():
    color("brown")

def Orange():
    color("orange")

def Black():
    color("Black")

def OriginalColor():
    color(pen_color)

def getColor():
    Color = askcolor()
    color_name = Color[1]
    colormode(255)
    color(color_name)

move_turtle()
speed(0)
color(pen_color)
listen()
##onkey(Color, "F10")
onkey(NewLetterDimensions, "k")
onkey(width1, "1")
onkey(width2, "2")
onkey(width3, "3")
onkey(width4, "4")
onkey(width5, "5")
onkey(width6, "6")
onkey(width7, "7")
onkey(width8, "8")
onkey(width9, "9")
onkey(width10, "0")
onkey(Blue, "F1")
onkey(Red, "F2")
onkey(DarkGreen, "F3")
onkey(Purple, "F4")
onkey(Pink, "F5")
onkey(Brown, "F6")
onkey(Orange, "F7")
onkey(Black, "F8")
onkey(getColor, "F9")
onkey(OriginalColor, "F10")
onscreenclick(goto)
onscreenclick(skip)
onkey(clear, "space")
onkey(back, "BackSpace")
onkey(walk, "Tab")
onkey(Up, "Up")
onkey(draw_H, "h")
onkey(bye, "Escape")
onkey(draw_E, "e")
onkey(draw_L, "l")
onkey(draw_O, "o")
onkey(draw_W, "w")
onkey(lambda: draw_R(letter_width, letter_height), "r")
onkey(lambda: draw_D(letter_width, letter_height), "d")
onkey(draw_newline, "Return")