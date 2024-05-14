#Source: https://stackoverflow.com/questions/48653466/how-to-avoid-typeerror-from-attempt-to-divide
#A program that allows people to enter information and calculate how much a tip should be
from graphics import *
import math
#setting up the window
win = GraphWin("Tip Calculator", 400, 400)
win.setBackground("teal")
#setting up the input
checksub = Text(Point(150, 150,), "What is the subtotal of the check?:")
checksub.draw(win)
checksub2 = Entry(Point(300,152), 5)
checksub2.draw(win)

tiprate = Text(Point(150,190), "What is the tip rate?:")
tiprate.draw(win)
tiprate2 = Entry(Point(250,190), 3)
tiprate2.draw(win)
#button
Buttontext = Text(Point(150,210), "Compute")
Buttontext.draw(win)
Buttonbox = Rectangle(Point(100,230),Point(200,199))
Buttonbox.draw(win)
#Calculations
win.getMouse()
tip = tiprate2.getText()
check = checksub2.getText()
float (taxsum = check / 4)
float (checktax = taxsum + check)
float (tipsum = checktax / tip)
float (checksum = (tipsum + checktax))
#presenting the output
tipoutput = Text(Point(150,250), "The tip rate is: tipsum")
tipoutput.draw(win)
checkoutput = Text(Point(150,260), "The Check total is: checksum")
checkoutput.draw(win)