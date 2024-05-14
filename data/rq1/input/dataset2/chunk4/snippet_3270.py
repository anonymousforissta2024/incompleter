#Source: https://stackoverflow.com/questions/68157511/typeerror-when-drawing-circle-in-pygame
from Box2D import (b2FixtureDef, b2CircleShape)

class Circle:
    def __init__(self, world, x, y, PPM):
        self.x = x / PPM
        self.y = y / PPM
        self.r = 1

        self.world = world
        self.body = self.world.CreateDynamicBody(
            position=(self.x, self.y),
            fixtures=b2FixtureDef(
                shape=b2CircleShape(radius = self.r), density=2.0, friction = 0.5))