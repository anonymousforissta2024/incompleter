#Source: https://stackoverflow.com/questions/36021430/getting-a-typeerror-for-unknown-reason
import pygame
import operator
pygame.init()
screen = pygame.display.set_mode((400, 711))
pygame.display.set_caption("INIX")
Calculator_Screen = pygame.image.load("Calculator.Screen.png")
op = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}
def calculator_module():

    events = list(pygame.event.get())
    for event in events:
        if event.type == pygame.QUIT:
            Calculator = False
            return Calculator
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if x > 17 and x < 107 and y > 445 and y < 530:     #1
                return "1"
            elif x > 108 and x < 198 and y > 445 and y < 530:     #2
                return "2"
            elif x > 199 and x < 290 and y > 445 and y < 530:     #3
                return "3"
            elif x > 17 and x < 107 and y > 336 and y < 443:     #4
                return "4"
            elif x > 108 and x < 198 and y > 336 and y < 443:     #5
                return "5"
            elif x > 199 and x < 290 and y > 336 and y < 443:     #6
                return "6"
            elif x > 17 and x < 107 and y > 268 and y < 334:     #7
                return "7"
            elif x > 108 and x < 198 and y > 268 and y < 334:     #8
                return "8"
            elif x > 199 and x < 290 and y > 268 and y < 334:     #9
                return "9"
            elif x > 17 and x < 107 and y > 532 and y < 620:     #0
                return "0"
            elif x > 199 and x < 290 and y > 532 and y < 620:     #=
                return "="
            elif x > 292 and x < 380 and y > 532 and y < 620:     #+
                return "+"
            elif x > 292 and x < 380 and y > 445 and y < 530:     #-
                return "-"
            elif x > 292 and x < 380 and y > 268 and y < 334:     #/
                return "/"
            elif x > 292 and x < 380 and y > 336 and y < 443:     #x
                return "*"

Calculator = True
while Calculator:
    screen.blit(Calculator_Screen, (0, 0))
    pygame.display.update()
    events = list(pygame.event.get())
    for event in events:
        if event.type == pygame.QUIT:
            Calculator = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if x > 180 and x < 218 and y > 670 and y < 708:
                Calculator = False

            while True:
                current = 0
                num1 = 0
                num2 = 0

                while current not in op:
                    num1 = num1*10 + int(current)
                    current = calculator_module()
                last_op = current
                current = 0
                while current != "=":
                    if current in op:
                        num1 = op[last_op](num1, num2)
                        last_op = current
                        num2 = 0
                    else:
                        num2 = num2*10 + int(current)
                    current = calculator_module()
                res = op[last_op](num1, num2)
                print(res)