#Source: https://stackoverflow.com/questions/39481039/typeerror-unsupported-operand-types-for-float-and-nonetype-in-python
import turtle as t
import math as m
import random as r

raindrops = int(input("Enter the number of raindrops: "))

def drawSquare():
    t.up()
    t.goto(-300,-300)
    t.down()
    t.fd(600)
    t.lt(90)
    t.fd(600)
    t.lt(90)
    t.fd(600)
    t.lt(90)
    t.fd(600)
    t.lt(90)

def location():
    x = (r.randint(-300, 300))
    y = (r.randint(-300, 300))
    t.up()
    t.goto(x, y)
    return x, y

def drawRaindrops(x, y):
    t.fillcolor(r.random(), r.random(), r.random())
    circles = (r.randint(3, 8))
    radius = (r.randint(1, 20))
    newradius = radius
    area = 0
    t.up()
    t.rt(90)
    t.fd(newradius)
    t.lt(90)
    t.down()
    t.begin_fill()
    t.circle(newradius)
    t.end_fill()
    t.up()
    t.lt(90)
    t.fd(newradius)
    t.rt(90)
    while circles > 0:
        if x + newradius < 300 and x - newradius > -300 and y + newradius < 300 and y - newradius > -300:
            t.up()
            t.rt(90)
            t.fd(newradius)
            t.lt(90)
            t.down()
            t.circle(newradius)
            t.up()
            t.lt(90)
            t.fd(newradius)
            t.rt(90)
            newradius += radius
            circles -= 1
            area += m.pi * radius * radius
        else:
            circles -= 1
    return area

def promptRaindrops(raindrops):
    if raindrops < 1 or raindrops > 100:
        print ("Raindrops must be between 1 and 100 inclusive.")
    if raindrops >= 1 and raindrops <= 100:
        x, y = location()
        area = drawRaindrops(x, y)
        area += promptRaindrops(raindrops - 1)
        return x, y, area

def main():
    t.speed(0)
    drawSquare()
    x, y, area = promptRaindrops(raindrops)
    print('The area is:', area, 'square units.')

main()
t.done()