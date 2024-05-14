#Source: https://stackoverflow.com/questions/19034714/pygame-typeerror-missing-1-required-positional-argument
import pygame,time,sys
from pygame import *



class pauseMenu():

    goToMenu = False
    imageDict = {}
    textDict = {}
    rectDict = {}
    Clicked_Button = ''
    DarkGrey =      (134, 134, 134)
    volume = 10
    FPSCLOCK = pygame.time.Clock()


    def pauseMenuFunct(self,screen,WINDIM):
        print("made it here")
        def check_collisions(self,pos,list):
        # iterate dict, check for collisions in systems
        #     print('Made it to teh da function')
            for k,v in list.items():
                # print('Made into to the for loop')
                if v.collidepoint(pos):
                    # print(v)
                    # print("clicked button:", k)
                    self.Clicked_Button = k
                    # print(self.Clicked_Button)
                    return True,k

        WINWIDTH,WINHEIGHT = WINDIM
        # print('Made it to the function')
        # screen.fill(background)
        imageDict = {'buttons': pygame.image.load('Resources/Pics/PauseOptions.png')
        }

        imageDict['buttons']=pygame.transform.smoothscale(imageDict['buttons'],(int(WINWIDTH*.2),(int(WINHEIGHT*.1))))

        buttonX,buttonY= imageDict['buttons'].get_size()
        # print(buttonX , buttonY)
        textSize = int(buttonY/2)
        # print(textSize)
        self.font = pygame.font.Font('Resources/chunkfont.ttf', textSize)
        textOptions  = self.font.render("Options", 1, self.DarkGrey)
        textSave     = self.font.render("Save", 1, self.DarkGrey)
        textQuit     = self.font.render("Quit", 1, self.DarkGrey)
        textVolume   = self.font.render("Volume", 1, self.DarkGrey)
        textBackToGame = self.font.render('Return', 1, self.DarkGrey)
        VolumePopUp  = self.font.render(str(self.volume), 1, self.DarkGrey)
        textBackToMenu = self.font.render('Menu', 1 , self.DarkGrey)


        self.rectDict['Options'] =           screen.blit(imageDict['buttons'], (WINWIDTH/4,(WINHEIGHT/3)))
        self.rectDict['Save'] =              screen.blit(imageDict['buttons'], (WINWIDTH/2+60.5,WINHEIGHT/3))
        self.rectDict['Quit'] =              screen.blit(imageDict['buttons'], (WINWIDTH/4,(WINHEIGHT/2)))
        self.rectDict['Volume'] =            screen.blit(imageDict['buttons'], ((WINWIDTH/2+60.5),(WINHEIGHT/2)))
        self.rectDict['Return'] =            screen.blit(imageDict['buttons'], (WINWIDTH/4,(WINHEIGHT/1.5)))
        self.rectDict['Menu'] =              screen.blit(imageDict['buttons'], (WINWIDTH/2+60.5,WINHEIGHT/1.5))
        self.textDict['textOptions'] =       screen.blit(textOptions,(WINWIDTH/4 + (buttonX/4),(WINHEIGHT/3+textSize/2)))
        self.textDict['textQuit'] =          screen.blit(textQuit,(WINWIDTH/4 + (buttonX/4),(WINHEIGHT/2+textSize/2)))
        self.textDict['textSave'] =          screen.blit(textSave,(WINWIDTH/2+60.5 + (buttonX/3),(WINHEIGHT/3+textSize/2)))
        self.textDict['textVolume'] =        screen.blit(textVolume,(WINWIDTH/2+50.5 + (buttonX/4.5),(WINHEIGHT/2+textSize/2)))
        self.textDict['textBacktoGame']=     screen.blit(textBackToGame,(WINWIDTH/4+ (buttonX/4),(WINHEIGHT/1.5+textSize/2)))
        self.textDict['textMenu']=           screen.blit(textBackToMenu,(WINWIDTH/2+60.5+ (buttonX/4),(WINHEIGHT/1.5+textSize/2)))
        self.textDict['volumeNum']=          screen.blit(VolumePopUp,(WINWIDTH/2+55.5 + buttonX/1.25,(WINHEIGHT/2+textSize/2)))
        pygame.display.update()
        print('made it to the update')


        while True:
            self.FPSCLOCK.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if check_collisions(self,event.pos,self.rectDict):

                            # print('Button Clicked from Event Loop is: '+self.Clicked_Button)

                            if self.Clicked_Button == 'Quit':
                                sys.exit()
                            elif self.Clicked_Button == 'Save':
                                print('It will be saved later')
                            elif self.Clicked_Button == 'Volume' and self.volume>0:
                                self.volume -= 1
                                print(self.volume)

                                VolumePopUp  = self.font.render(str(self.volume), 1, self.DarkGrey)
                                screen.blit(imageDict['buttons'], ((WINWIDTH/2+60.5),(WINHEIGHT/2)))
                                screen.blit(VolumePopUp,(WINWIDTH/2+55.5 + buttonX/1.25,(WINHEIGHT/2+textSize/2)))

                                pygame.display.update(self.textDict['volumeNum'])


                            elif self.Clicked_Button == 'Return':
                                print('This will close the menu and you return you to the game.')
                            elif self.Clicked_Button == 'Options':
                                print('This will take you to an options screen')
                                #TODO Return values
                            elif self.Clicked_Button == 'Menu':
                                print('Will take you to main menu sooner or later')
                    elif event.button == 3:
                        if check_collisions(self,event.pos,self.rectDict):
                            if self.Clicked_Button == 'Volume' and self.volume<10:
                                self.volume += 1
                                print(self.volume)

                                VolumePopUp  = self.font.render(str(self.volume), 1, self.DarkGrey)
                                screen.blit(imageDict['buttons'], ((WINWIDTH/2+60.5),(WINHEIGHT/2)))
                                screen.blit(VolumePopUp,(WINWIDTH/2+55.5 + buttonX/1.25,(WINHEIGHT/2+textSize/2)))

                                pygame.display.update(self.textDict['volumeNum'])

                                #TODO Return volume values


    def __init__(self):
        print('PauseMenu _init_ ran')