#Source: https://stackoverflow.com/questions/67366029/win-display-blitrightimg-arrx-20-arry-20-attributeerror-pygame-surface-o
import pygame, sys, random

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Python Night Funkin'")

upImg = pygame.image.load("up.png")
downImg = pygame.image.load("down.png")
rightImg = pygame.image.load("right.png")
leftImg = pygame.image.load("left.png")


test = 0
x = 0
y = 0
arrX = 0
arrY = 0
height = 500
width = 500
arrHeight = 20
arrWidth = 20
arrSpeed = 5

def drawWindow():
    win.fill((0,0,0))
    pygame.draw.rect(win, (20,20,20), (70,370, 60, 60))
    pygame.draw.rect(win, (20,20,20), (170,370, 60, 60))
    pygame.draw.rect(win, (20,20,20), (270,370, 60, 60))
    pygame.draw.rect(win, (20,20,20), (370,370, 60, 60))
    pygame.draw.rect(win, (255, 0, 0), (x-20, y-20, 40, 40))
    if arrX == 100:
        win.display.blit(rightImg, (arrX-20,arrY-20))
    if arrX == 200:
        win.display.blit(downImg, (arrX-20,arrY-20))
    if arrX == 300:
        win.display.blit(upImg, (arrX-20,arrY-20))
    if arrX == 400:
        win.display.blit(leftImg, (arrX-20,arrY-20))
    pygame.display.update()
clock = pygame.time.Clock();

run = True
arrowX = [100, 200, 300, 400]
Arrow = []
while run:
    clock.tick(30);
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False