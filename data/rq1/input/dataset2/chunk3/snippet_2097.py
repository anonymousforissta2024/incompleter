#Source: https://stackoverflow.com/questions/51731348/how-to-access-attributes-of-the-groups-object-attributeerror-group-object-h
import pygame

class GeoFence(pygame.sprite.Sprite):
    def __init__(self, rect, risk_level, *groups):
        # we set a _layer attribute before adding this sprite to the sprite groups
        self._layer = 1
        pygame.sprite.Sprite.__init__(self, groups)
        self.image = pygame.surface.Surface((rect.width, rect.height))
        self.image.fill(GREEN)
        self.rect = rect
        self.risk_level = risk_level


class Worker(pygame.sprite.Sprite):

  # we introduce to possible states: RUNNING and IDLE
  RUNNING = 0
  IDLE = 1
  NUMBER_OF_ACCIDENTS = 0

  def __init__(self, image_running, image_idle, location, *groups):

    # each state has it's own image
    self.images = {
        Worker.RUNNING: pygame.transform.scale(get_image(image_running), (45, 45)),
        Worker.IDLE: pygame.transform.scale(get_image(image_idle), (20, 45))
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

    if length == 0 or speed == 0:
        new_state = Worker.IDLE
        self.direction = pygame.math.Vector2(0, 0)
    else:
        new_state = Worker.RUNNING
        self.direction = vec.normalize()

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

    if any(s for s in pygame.sprite.spritecollide(self, fences, False) if s != self):
        print("RISK_LEVEL: ",fences.risk_level)


all_sprites = pygame.sprite.LayeredUpdates()
workers = pygame.sprite.Group()
fences = pygame.sprite.Group()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("TEST")

# create multiple workers
for pos in ((30,30), (50, 400), (200, 100), (700, 200)):
    Worker("w1.png", "w2.png", pos, all_sprites, workers, fences)

# create multiple geo-fences
risks = ["HIGH","MEDIUM","LOW"]
for rect in (pygame.Rect(510,150,75,52), pygame.Rect(450,250,68,40), pygame.Rect(450,370,68,48)):
    risk = risks[random.randint(0,2)]
    GeoFence(rect, risk, all_sprites, fences)