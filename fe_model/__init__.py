import block
import character
import wall
from variables import *

class Model:
    """Encodes game state."""
    def __init__(self):
        self.ref = 50
        self.swidth = 15 * self.ref
        self.sheight = 15 * self.ref
        self.grid = {}
        # self.characters=pygame.sprite.Group()
        self.character = character.Character(self,'Player',1,2,3,4,5,6,7,350,350)
        # self.populateBlocks()
        # self.populateCharaceters()
        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                node = (x,y)
                self.grid[(x,y)] = node  
        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                if x not in range(3 * self.ref, self.swidth - 3*self.ref,self.ref) or y not in range(3*self.ref, self.sheight-3*self.ref, self.ref):
                    boundary = block.Outeredge(x,y)
                    self.grid[(boundary.rect.x,boundary.rect.y)] = boundary
        # print self.grid

    def update(self, mx, my):
        pass