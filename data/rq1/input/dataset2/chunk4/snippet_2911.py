#Source: https://stackoverflow.com/questions/72136240/how-to-fix-colorred-nameerror-name-color-is-not-defined
import turtle 
color('red')
bgcolor('black')
speed(20)
b = 200
while b > 0:
    left(b)
    forward(b+3)
    b -= 1