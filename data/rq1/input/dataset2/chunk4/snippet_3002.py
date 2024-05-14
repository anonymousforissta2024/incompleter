#Source: https://stackoverflow.com/questions/63819205/self-rect-pygame-rectx-y-width-height-typeerror-argument-must-be-rect-style
import pygame
pygame.init()

# Build The Screen
window = pygame.display.set_mode((700,500))

# Name Screen
pygame.display.set_caption("Noobs first Game")

bg = pygame.image.load("skybg1.png")
bg_shift = 0


# Class Player
class player:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 4
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
        self.ss1 = pygame.image.load("heroplane1.png")
        self.ss1 = pygame.transform.scale(self.ss1,(self.ss1.get_width()//9,self.ss1.get_height()//9))
    def draw(self):
        self.rect.topleft=(self.x,self.y)
        pygame.draw.rect(window,self.color,self.rect)

        player_rect = self.ss1.get_rect(center = self.rect.center)
        player_rect.centerx += -7
        player_rect.centery += -6
        window.blit(self.ss1,player_rect)

# Class Enemy
class enemy:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 4
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
        self.ss1 = pygame.image.load("enemyplane1.png")
        self.ss1 = pygame.transform.scale(self.ss1,(self.ss1.get_width()//9,self.ss1.get_height()//9))
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(window,self.color,self.rect)

        enemy_rect = self.ss1.get_rect(center = self.rect.center)
        enemy_rect.centerx += -2
        enemy_rect.centery += -6
        window.blit(self.ss1,enemy_rect)


# Class Enemy2
class enemy2:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
        self.ss1 = pygame.image.load("enemyplane2.png")
        self.ss1 = pygame.transform.scale(self.ss1,(self.ss1.get_width()//9,self.ss1.get_height()//9))
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(window,self.color,self.rect)

        enemy2_rect = self.ss1.get_rect(center = self.rect.center)
        enemy2_rect.centerx += -4
        enemy2_rect.centery += -6
        window.blit(self.ss1,enemy2_rect)


# Class Enemy3
class enemy3:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
        self.ss1 = pygame.image.load("enemyplane3.png")
        self.ss1 = pygame.transform.scale(self.ss1,(self.ss1.get_width()//9,self.ss1.get_height()//9))
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(window,self.color,self.rect)

        enemy3_rect = self.ss1.get_rect(center = self.rect.center)
        enemy3_rect.centerx += -4
        enemy3_rect.centery += -6
        window.blit(self.ss1,enemy3_rect)



class projectile(object):
   def __init__(self, x, y,color):
       self.x = x
       self.y = y
       self.slash = pygame.image.load("herogun1.png")
       self.rect  = self.slash.get_rect()
       self.rect.topleft = ( self.x, self.y )
       self.speed = 10
       self.color = color

   def draw(self, window):
       self.rect.topleft = ( self.x,self.y )

       window.blit(slash, self.rect)


class enemygun:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
        self.ss1 = pygame.image.load("enemygun1.png")
        self.ss1 = pygame.transform.scale(self.ss1,(self.ss1.get_width()//11,self.ss1.get_height()//11))
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(window,self.color,self.rect)

        enemy3_rect = self.ss1.get_rect(center = self.rect.center)
        enemy3_rect.centerx += -7
        enemy3_rect.centery += -2
        window.blit(self.ss1,enemy3_rect)



        
# Color
white = (255,255,255)

# Draw Player
playerman = player(5,250,90,40,white)

# For Enemy
enemy1 = enemy(400,100,90,40,white)
enemy4 = enemy(400,400,90,40,white)

# For Enemy2
enemy21 = enemy2(400,300,90,40,white)

# For Enemy3
ememy31 = enemy3(400,400,90,40,white)

egun1 = enemygun(250,300,30,20,white)

enemys = [enemy1,enemy4]


# enemys
enemyGroup = pygame.sprite.Group()
level1 = [
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",
"                     1",]


for iy, row in enumerate(level1):
    for ix, col in enumerate(row):
        if col == "1":
            new_enemy = enemy(ix*70,iy*70,90,40,(255,255,255))
            enemys.append(new_enemy)



# Redrawwinodw
def redrawwindow():
    window.fill((0,0,0))

    bg_width = bg.get_width()
    bg_offset = bg_shift % bg_width 
    
    window.blit(bg, (-bg_offset, 0)) 
    window.blit(bg, (bg_width - bg_offset, 0))

    
    # Draw playerman
    playerman.draw()

    # Draw enemy
    for enemy in enemys:
        enemy.draw()

    # Draw enemy2
    enemy21.draw()

    # Draw enemy3
    ememy31.draw()


    # Draw enemygun
    egun1.draw()
 





# FPS Cnd Clock
fps = (30)
clock = pygame.time.Clock()


bullets = []

# Main Loop
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
         
        for bullet in bullets:
            if bullet.x < 500 and bullet.x > 0:
                 bullet.x += bullet.speed 
            else:
                bullets.pop(bullets.index(bullet))
        if len(bullets) < 2:  
                bullets.append(projectile(round(playerman.x+playerman.width//2),round(playerman.y + playerman.height-54),(0,0,0)))



    for enemy in enemys:
        enemy.x -= enemy.speed
    


    bg_shift += round(3/2)


    # Keys For Playerman
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and playerman.x > playerman.speed:
        playerman.x -= playerman.speed
       
        

    if keys[pygame.K_d] and playerman.x < 260 - playerman.width - playerman.speed:
        playerman.x += playerman.speed


    if keys[pygame.K_w] and playerman.y > playerman.speed:
        playerman.y -= playerman.speed


    if keys[pygame.K_s] and playerman.y < 500 - playerman.height - playerman.speed:
        playerman.y += playerman.speed


    if keys[pygame.K_SPACE]:
        if playerman.left:
            facing = -1
        else:
            facing = 1

    if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
        bullets.append(player(round(playerman.x+playerman.width//2), round(playerman.y + playerman.height//2), 6, (255,255,255), white)) 

            
# Update And Other Sutff    
    redrawwindow()
    for bullet in bullets:
        bullet.draw()

    
    pygame.display.update()
pygame.quit()
        