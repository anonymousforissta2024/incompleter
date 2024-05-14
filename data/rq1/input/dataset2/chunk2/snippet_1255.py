#Source: https://stackoverflow.com/questions/65533434/python-setattr-causes-attribute-error-on-a-defined-variable
import pygame as pg


class Block:
    blocks = {}
    id_ = 1

    def __init__(self, surface, name=None, color=[0] * 3, width=0):
        self.surface = surface
        self.name = (name if name else Block.id_)
        self.color = color
        self.width = width

        self.rect = pg.Rect((0, 0), [20] * 2)
        self.block = self.make_block()

        pg.draw.polygon(*self.block)

        Block.blocks[self.name] = self

        if not name:
            Block.id_ += 1

    def make_block(self):
        point_1 = self.rect.topleft
        point_2 = (self.rect.topleft[0], self.rect.topleft[1] + self.rect.size[1])
        point_3 = (point_2[0] + self.rect.size[0], point_2[1])
        point_4 = (point_3[0], point_1[0])

        return [self.surface, self.color, (point_1, point_2, point_3, point_4), self.width]

    def __setattr__(self, name, value):
        pass


Block(pg.Surface((20, 20)))