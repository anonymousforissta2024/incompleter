#Source: https://stackoverflow.com/questions/70399617/attribute-error-list-object-has-no-attribute-checkclick
from os import access
import pygame,sys
from random import randrange
import numpy
#Constants
Columns =5
Rows = 5
X,Y = 320,0

class Button:
   def __init__(self,x,y,image,scale):
       self.x = x
       self.y=y
       self.image = pygame.transform.scale(image,(scale,scale))
       self.scale = scale
       self.rect = self.image.get_rect(topleft=(x,y))
       self.clicked = False 
       self.Action = False

   
   def Draw(self):
       Win.blit(self.image,(self.x,self.y))
   
   def CheckClick(self):
       isClicked = False
       mousepos= pygame.mouse.get_pos()
       if self.rect.collidepoint(mousepos):
           if pygame.mouse.get_pressed()[0] ==1 and self.clicked == False:
               self.clicked = True
               self.Action = True
           if pygame.mouse.get_pressed()[0] ==0:
               self.clicked = False
       return self.Action



#Win
WinWidth, WinHeight = 1280,800
Win = pygame.display.set_mode((WinWidth,WinHeight))

#IMAGES
test_img = pygame.image.load("test.png")
red_img = pygame.image.load("Red.png")
green_img = pygame.image.load("green.png")
blue_img = pygame.image.load("blue.png")

#Board
Board = [[ randrange(0,3) for column in range(Columns)] for row in range(Rows) ]

BoardObjs = []

BoardXYs = [[None for column in range(Columns)]for row in range(Rows)]

#Fill BoardXYS
for k in range(len(Board)):
   for j in range(len(Board[1])):
       BoardXYs[k][j] = [X,Y]
       X += 160
   X = 320
   Y += 160

for r in range(len(Board)):
   for t in range(len(Board[1])):
       if Board[r][t] == 0:
           BoardObjs.append(Button(BoardXYs[r][t][0],BoardXYs[r][t][1],red_img,100))
       if Board[r][t] == 1:
           BoardObjs.append(Button(BoardXYs[r][t][0],BoardXYs[r][t][1],green_img,100))
       if Board[r][t] == 2:
           BoardObjs.append(Button(BoardXYs[r][t][0],BoardXYs[r][t][1],blue_img,100))



BoardObjs = [[BoardObjs[0],BoardObjs[1],BoardObjs[2],BoardObjs[3],BoardObjs[4]],
           [BoardObjs[5],BoardObjs[6],BoardObjs[7],BoardObjs[8],BoardObjs[9]],
           [BoardObjs[10],BoardObjs[11],BoardObjs[12],BoardObjs[13],BoardObjs[14]],
           [BoardObjs[15],BoardObjs[16],BoardObjs[17],BoardObjs[18],BoardObjs[19]],
           [BoardObjs[20],BoardObjs[21],BoardObjs[22],BoardObjs[23],BoardObjs[24]]]

print(len(Board))
print(len(BoardObjs))


#Images
img_0 = pygame.Rect(0,0,64,64)

TouchingReds = 0
def CheckMatches(Board):
   VerticalMatch = False
   HorizontalMatch = False
   for m in range(len(Board)):
       for n in range(len(Board[1])-2):
           if Board[m][n]==Board[m][n+1]==Board[m][n+2]:
               HorizontalMatch = True
               Board[m][n] = None
               Board[m][n+1] = None
               Board[m][n+2] = None
               BoardObjs[m][n] = None
               BoardObjs[m][n+1] = None
               BoardObjs[m][n+2] = None
       for o in range(len(Board[1])-2):
           for u in range(len(Board)):
               if Board[o][u]==Board[o+1][u]==Board[o+2][u]:
                   VerticalMatch = True
                   Board[o][u] = None
                   Board[o+1][u] = None
                   Board[o+2][u] = None
                   BoardObjs[o][u] = None
                   BoardObjs[o+1][u] = None
                   BoardObjs[o+2][u] = None
       

def Draw(Board,BoardXYs):
   DoAppend = True
   Win.fill((255,255,255))
   for y in range(len(BoardObjs)):
       for u in range(len(BoardObjs[1])):
           if BoardObjs[y][u] != None:
               BoardObjs[y][u].Draw()
   pygame.display.update()

def Swap():
   FirstClick = False
   for i in range(len(BoardObjs)):
       for t in range(len(BoardObjs[1])):
           if BoardObjs[i][t] != None:
               if BoardObjs[i][t].CheckClick and FirstClick == True:
                   BoardObjs[num][num2]=BoardObjs[i][t]
                   BoardObjs[i][t]=Buffer
                   FirstClick = False
               print(BoardObjs[i][t])
           if BoardObjs[i][t] !=None:
               if BoardObjs[i][t].CheckClick:
                   Buffer  = BoardObjs[i]
                   num =i
                   num2 = t
                   FirstClick = True
#ZEROS - RED
#ONES - GREEN
#TWOS - BLUE

clock = pygame.time.Clock()
def GameLoop():
   run = True
   while run:
       clock.tick(60)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
       CheckMatches(Board)
       Draw(Board,BoardXYs)
       Swap()
   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   GameLoop()