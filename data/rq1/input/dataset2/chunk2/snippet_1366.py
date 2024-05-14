#Source: https://stackoverflow.com/questions/51813378/attributeerror-worker-object-has-no-attribute-idf
import pygame, random
import sys

WHITE = (255, 255, 255)
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH=1000
SCREENHEIGHT=578

IMG_BACKGROUND = "background.jpg"
IMG_WORKER_RUNNING = "images/workers/worker_1.png"
IMG_WORKER_IDLE = "images/workers/worker_2.png"
IMG_WORKER_ACCIDENT = "images/workers/accident.png"


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, *groups):
        # we set a _layer attribute before adding this sprite to the sprite groups
        # we want the background to be actually in the back
        self._layer = -1
        pygame.sprite.Sprite.__init__(self, groups)
        # let's resize the background image now and only once
        self.image = pygame.transform.scale(pygame.image.load(image_file).convert(), (SCREENWIDTH, SCREENHEIGHT))
        self.rect = self.image.get_rect(topleft=location)


class GeoFence(pygame.sprite.Sprite):
    def __init__(self, idf, rect, risk_level, *groups):
        # we set a _layer attribute before adding this sprite to the sprite groups
        self._layer = 1
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = pygame.surface.Surface((rect.width, rect.height))
        self.image.fill(GREEN)
        self.rect = rect
        self.idf = idf
        self.risk_level = risk_level
        self.font = pygame.font.SysFont('Arial', 20)
        text = self.font.render(risk_level, 1, (255,0,0), GREEN)
        text_rect = text.get_rect(center=(rect.width/2, rect.height/2))
        self.image.blit(text, text_rect)



class Worker(pygame.sprite.Sprite):

    # we introduce to possible states: RUNNING and IDLE
    RUNNING = 0
    IDLE = 1
    ACCIDENT = 2
    NUMBER_OF_ACCIDENTS = 0
    image_cache = {}

    def __init__(self, image_running, image_idle, image_accident, location, *groups):

        self.font = pygame.font.SysFont('Arial', 10)

        # each state has it's own image
        self.images = {
            Worker.RUNNING: pygame.transform.scale(self.get_image(image_running), (45, 45)),
            Worker.IDLE: pygame.transform.scale(self.get_image(image_idle), (20, 45)),
            Worker.ACCIDENT: pygame.transform.scale(self.get_image(image_accident), (40, 40))
        }

        # we set a _layer attribute before adding this sprite to the sprite groups
        # we want the workers on top
        self._layer = 2
        pygame.sprite.Sprite.__init__(self, groups)

        # let's keep track of the state and how long we are in this state already            
        self.state = Worker.IDLE
        self.ticks_in_state = 0

        self.image = self.images[self.state]
        self.rect = self.image.get_rect(topleft=location)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = random.randint(1, 3)
        self.set_random_direction()


    def set_random_direction(self):
        # random new direction or standing still
        vec = pygame.math.Vector2(random.randint(-100,100), random.randint(-100,100)) if random.randint(0, 5) > 1 else pygame.math.Vector2(0, 0)

        # check the new vector and decide if we are running or fooling around
        length = vec.length()
        speed = sum(abs(int(v)) for v in vec.normalize() * self.speed) if length > 0 else 0

        if (length == 0 or speed == 0) and (self.state != Worker.ACCIDENT):
            new_state = Worker.IDLE
            self.direction = pygame.math.Vector2(0, 0)
        elif self.state != Worker.ACCIDENT:
            new_state = Worker.RUNNING
            self.direction = vec.normalize()
        else:
            new_state = Worker.ACCIDENT

        self.ticks_in_state = 0
        self.state = new_state

        # use the right image for the current state
        self.image = self.images[self.state]


    def update(self, screen):
        self.ticks_in_state += 1
        # the longer we are in a certain state, the more likely is we change direction
        if random.randint(0, self.ticks_in_state) > 70:
            self.set_random_direction()

        # now let's multiply our direction with our speed and move the rect
        vec = [int(v) for v in self.direction * self.speed]
        self.rect.move_ip(*vec)

        # if we're going outside the screen, change direction
        if not screen.get_rect().contains(self.rect):
            self.direction = self.direction * -1

        # Check distances between workers and fences
        w_dist = {}
        for w in workers:
            f_dist = {}
            for f in fences:
                if f != self:
                    distance_meters = self.rect_distance(w.rect, f.rect)
                    f_dist_meters[f.idf] = distance
            w_dist[w.idw] = f_dist
        pygame.display.set_caption(str(w_dist[1][1]))

        # Risk handling
        self.handle_risks()

        self.rect.clamp_ip(screen.get_rect())


    def handle_risks(self):
        for s in pygame.sprite.spritecollide(self, fences, False):
            if s != self:
                self.speed = 0
                self.state = Worker.ACCIDENT
                self.image = self.images[self.state]
                Worker.NUMBER_OF_ACCIDENTS += 1


    # Distance between workers and geo-fences
    def rect_distance(self, rect1, rect2):
        x1, y1 = rect1.topleft
        x1b, y1b = rect1.bottomright
        x2, y2 = rect2.topleft
        x2b, y2b = rect2.bottomright
        left = x2b < x1
        right = x1b < x2
        top = y2b < y1
        bottom = y1b < y2
        if bottom and left:
            return math.hypot(x2b-x1, y2-y1b)
        elif left and top:
            return math.hypot(x2b-x1, y2b-y1)
        elif top and right:
            return math.hypot(x2-x1b, y2b-y1)
        elif right and bottom:
            return math.hypot(x2-x1b, y2-y1b)
        elif left:
            return x1 - x2b
        elif right:
            return x2 - x1b
        elif top:
            return y1 - y2b
        elif bottom:
            return y2 - y1b
        else:
            return 0


    def get_image(self,key):
        if not key in image_cache:
            image_cache[key] = pygame.image.load(key)
        return image_cache[key]


pygame.init()

all_sprites = pygame.sprite.LayeredUpdates()
workers = pygame.sprite.Group()
fences = pygame.sprite.Group()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("TEST")

# create multiple workers
for pos in ((30,30), (50, 400), (200, 100), (700, 200)):
    Worker(IMG_WORKER_RUNNING, IMG_WORKER_IDLE, IMG_WORKER_ACCIDENT, pos, all_sprites, workers, fences)

# create multiple geo-fences
idf = 1
risks = ["H","M","L"]
for rect in (pygame.Rect(510,150,75,52), pygame.Rect(450,250,68,40), pygame.Rect(450,370,68,48),
             pygame.Rect(0,0,20,SCREENHEIGHT),pygame.Rect(0,0,SCREENWIDTH,20),
             pygame.Rect(SCREENWIDTH-20,0,20,SCREENHEIGHT),pygame.Rect(0,SCREENHEIGHT-20,SCREENWIDTH,20)):
    risk = risks[random.randint(0,2)]
    GeoFence(idf, rect, risk, all_sprites, fences)
    idf += 1

# and the background
Background(IMG_BACKGROUND, [0,0], all_sprites)

carryOn = True
clock = pygame.time.Clock()
while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn = False
            pygame.display.quit()
            pygame.quit()
            quit()

    all_sprites.update(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(20)