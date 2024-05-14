#Source: https://stackoverflow.com/questions/57246202/how-to-fix-attributeerror-class-object-has-no-attribute-rect
def apartment_movement():

    keys = pygame.key.get_pressed()

    boundary = pygame.sprite.spritecollide(scarn, apartment_walls, False, False)

    if boundary:
        scarn.left = False
        scarn.right = False
        scarn.up = False
        scarn.down = False
        scarn.standing = False
        scarn.sleeping = False
    if not boundary:
        if keys[pygame.K_LEFT] and scarn.x > 110 - scarn.width - scarn.vel:  # allows the player to move left
            scarn.x -= scarn.vel
            scarn.left = True
            scarn.right = False
            scarn.up = False
            scarn.down = False
            scarn.standing = False
            scarn.sleeping = False
        elif keys[pygame.K_RIGHT] and scarn.x < 795 - scarn.width - scarn.vel:  # allows the player to move right
            scarn.x += scarn.vel
            scarn.right = True
            scarn.left = False
            scarn.up = False
            scarn.down = False
            scarn.standing = False
            scarn.sleeping = False
        elif keys[pygame.K_UP] and scarn.y > 130 - scarn.height - scarn.vel:
            scarn.y -= scarn.vel
            scarn.up = True
            scarn.right = False
            scarn.left = False
            scarn.down = False
            scarn.standing = False
            scarn.sleeping = False
        elif keys[pygame.K_DOWN] and scarn.y < 540 - scarn.height - scarn.vel:
            scarn.y += scarn.vel
            scarn.down = True
            scarn.right = False
            scarn.left = False
            scarn.up = False
            scarn.standing = False
            scarn.sleeping = False
        else:  # clarifies the player is not moving left or right
            scarn.walkCount = 0


class apartment_walls(pygame.sprite.Sprite):  # creates the walls of the apartment (1st scene)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.boundary1 = pygame.Rect(243, 60, 8, 275)
        self.boundary2 = pygame.Rect(510, 60, 8, 275)
        self.boundary3 = pygame.Rect(243, 421, 215, 5)
        self.boundary4 = pygame.Rect(243, 330, 220, 5)
        self.boundary5 = pygame.Rect(510, 421, 145, 5)
        self.boundary6 = pygame.Rect(510, 330, 145, 5)
        self.boundary7 = pygame.Rect(700, 421, 57, 5)
        self.boundary8 = pygame.Rect(700, 330, 57, 5)
        self.boundary9 = pygame.Rect(43, 410, 120, 10)
        self.boundary10 = pygame.Rect(510, 335, 5, 90)
        self.boundary11 = pygame.Rect(460, 335, 5, 90)
        self.boundary12 = pygame.Rect(700, 335, 5, 90)
        self.boundary13 = pygame.Rect(650, 335, 5, 90)


def draw_apartment():  # draws the apartment (1st scene)

    win.blit(bg, (0, 0))
    win.blit(bed, (322, 120))

    pygame.draw.rect(win, black, (200, 470, 100, 10), 0)
    pygame.draw.polygon(win, black, [(180, 473), (200, 488), (200, 458)], 0)

    scarn.draw(win)


class Scarn(pygame.sprite.Sprite):  # creates attributes for Michael Scarn (player)

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        # loads sprites for animations
        self.rect = pygame.Rect(pygame.image.load('Michael Scarn Forward Standing.png')), pygame.Rect(
            pygame.image.load('Michael Scarn Backward Standing.png')), pygame.Rect(
            [pygame.image.load('Michael Scarn Up 1.png'), pygame.image.load('Michael Scarn Up 2.png')]), [
                        pygame.image.load('Michael Scarn Down 1.png'), pygame.image.load('Michael Scarn Down 2.png')], [
                        pygame.image.load('Michael Scarn Right 1.png'), pygame.image.load('Michael Scarn Right 2.png'),
                        pygame.image.load('Michael Scarn Right 3.png'),
                        pygame.image.load('Michael Scarn Right 4.png')], [pygame.image.load('Michael Scarn Left 1.png'),
                                                                          pygame.image.load('Michael Scarn Left 2.png'),
                                                                          pygame.image.load('Michael Scarn Left 3.png'),
                                                                          pygame.image.load(
                                                                              'Michael Scarn Left 4.png')], pygame.image.load(
            'Michael Scarn Sleeping.png')