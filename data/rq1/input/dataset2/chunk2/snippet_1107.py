#Source: https://stackoverflow.com/questions/45897466/typeerror-pygame-surface-object-is-not-callable-pygame-module
def town ():
    global outTown
    while not outTown:
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            print (event)
                            mx, my = pygame.mouse.get_pos()
                            mx = mx + my
                            if 375 <= mx <= 448:
                                    outTown = True
                                    print ("OK!")
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

            houseSpr1 = pygame.image.load ('houseD.png') # default house img
            houseSpr1(0,250)
            gameDisplay.fill(green) # background
            pygame.draw.rect(gameDisplay,grey,(0,400,1280,50)) # main path
            pygame.draw.rect(gameDisplay,grey,(200,125,50,280)) # branch path
            player(x,y)
            pygame.display.update()
            clock.tick(60)

def houseSpr1(a,b):
    gameDisplay.blit(houseSpr1, (0,250))

def house1():
    global outHouse
    while not outHouse:
            gameDisplay.fill(black)
town()
houseSpr1()
gameIntro()
house1()
pygame.quit()
quit()