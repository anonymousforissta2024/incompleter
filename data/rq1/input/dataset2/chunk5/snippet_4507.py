#Source: https://stackoverflow.com/questions/60030733/nameerror-within-inheritance
class camera(player):
    def __init__(self, stagePosX,playerposX,y):
        super(camera,self).__init__(playerposX,characterPosX,y)
        self.playerposX = playerposX
        self.startscrolling = bgWidth / 2
        self.stagePosX = stagePosX
        self.rel_x = 0


    def scroll(self,stagePosX):
        if self.k[pygame.K_LEFT]:
            self.vel = (self.vel*-1)
        elif self.k[pygame.K_RIGHT]:
            self.vel = (self.vel*1)
        else:
            self.vel = 0



        self.rel_x = self.stagePosX % bgWidth
        if self.playerPosX > stageWidth - self.width:
            self.playerPosX = self.stageWidth - self.width  # If the player position exceeds the stage
        if self.playerposX < 0 - self.width:
            self.playerposX = self.width  # If the player position is far left
        if self.playerposX < self.startscrolling:
            self.characterPosX = self.playerposX
        elif self.playerposXplayerposX > stageWidth - self.startscrolling:
            self.characterPosX = self.playerPosX - stageWidth + self.width
        else:
            self.characterPosX = self.startscrolling
            self.stagePosX +=  -self.vel






    def draw(self, win):
        win.blit(bg, (self.rel_x - bgWidth, 0))
        if self.rel_x < bgWidth:
            win.blit(bg, (self.rel_x, 0))