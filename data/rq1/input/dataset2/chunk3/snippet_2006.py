#Source: https://stackoverflow.com/questions/57099307/attributeerror-type-object-projectile-has-no-attribute-dir
class player():
    x = WIDTH / 2
    y = HEIGHT / 2
    width = 50
    height = 50
    speed = 1

    def draw(self):
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))

class projectile():

    radius = 10
    speed = 8

    def __init__(self, x, y, dir={}):
        self.x = x
        self.y = y
        self.dir = dir

    def shot(self):
        for bullet in bullets:
            if self.dir == 'N':
                print('N')
                self.y -= 1
            if self.dir == 'W':
                print('W')
                self.x -= 1
            if self.dir == 'S':
                print('S')
                self.y += 1
            if self.dir == 'E':
                print('E')
                self.x += 1

    def draw(self):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.radius)


def get_input():
    keys = pygame.key.get_pressed()
    ev = pygame.event.get()

    if keys[pygame.K_w]:
        player.y -= player.speed
        projectile.dir == 'N'
    if keys[pygame.K_a]:
        player.x -= player.speed
        projectile.dir == 'W'
    if keys[pygame.K_s]:
        player.y += player.speed
        projectile.dir == 'S'
    if keys[pygame.K_d]:
        player.x += player.speed
        projectile.dir == 'E'
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(projectile(round(player.x + player.width//2), round(player.y + player.height//2), dir))


def update():
    clock.tick(300)
    win.fill ((0, 0, 0))
    get_input()
    player.draw()
    for bullet in bullets:
        bullet.draw()
        bullet.shot()
    pygame.display.update()


running = True
player = player()
bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

#pygame.quit()