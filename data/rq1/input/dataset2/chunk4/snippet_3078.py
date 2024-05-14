#Source: https://stackoverflow.com/questions/66087209/dictionary-typeerror-list-indices-must-be-integers-or-slices-not-str
import pygame

textures = {"on_start.png":"(pygame image)","print.png":"(pygame image)"}

class block(pygame.sprite.Sprite):
    def __init__(self,initx,inity,initp,initty,initte,initid):
        super().__init__()
        self.xpos = initx
        self.ypos = inity
        self.parent = initp
        self.blockType = initty
        self.texture = textures[initte]
        self.blockID = initid
        block_loop.add(self)

def load():
    global block_loop, block_store, blockNumber
    block_store = []
    block_loop = pygame.sprite.Group()
    pend1 = {"next":2,"0":{"type":"on_start","x":50,"y":50,"parent":-1},"1":{"type":"print","x":0,"y":0,"parent":0}}
    blockNumber = pend1["next"]
    del pend1["next"]
    for item in pend1:
        #print(pend1[item]["x"],pend1[item]["y"],pend1[item]["parent"],pend1[item]["type"],pend1[item]["type"] + ".png",item)
        block_store[item] = block(pend1[item]["x"],pend1[item]["y"],pend1[item]["parent"],pend1[item]["type"],pend1[item]["type"] + ".png",item)

load()