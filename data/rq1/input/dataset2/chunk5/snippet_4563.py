#Source: https://stackoverflow.com/questions/60326330/need-help-resolving-attribute-error-within-pygameinheritance
class projectile(player):
    def __init__(self,bulletx, bullety):
        self.bulletx = bulletx
        self.bullety = bullety
        self.facing = 1
        self.shooting = False
    def shoot(self):
        self.vel = 30 * self.facing
        if self.left:
            self.facing = -1
        else:
            self.facing = 1
        self.bulletx += self.vel
        if self < 0 or bullet.x > 500:
            self.shooting = True
    def draw(self):
     if self.shooting == True:
         win.blit(thunderball,(self.bulletx,self.bullety))