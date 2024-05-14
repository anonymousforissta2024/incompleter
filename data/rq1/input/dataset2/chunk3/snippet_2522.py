#Source: https://stackoverflow.com/questions/40072913/attributeerror-in-a-pygame-sprite-sprite-subclass
class Entity(pygame.sprite.Sprite):
    entitiesTop = pygame.sprite.Group()
    entitiesMid = pygame.sprite.Group()
    entitiesBot = pygame.sprite.Group()
    entities = [entitiesBot, entitiesMid, entitiesTop]

    def __init__(self, force = None):
        pygame.sprite.Sprite.__init__(self)
        if force is None:
            if isinstance(self, Platform):
                Entity.entitiesTop.add(self)
            elif isinstance(self, (Bullet, Gun)):
                Entity.entitiesMid.add(self)
            else:
                Entity.entitiesBot.add(self)
        else:
            Entity.entities[force].add(self)